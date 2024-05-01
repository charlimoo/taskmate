# Import necessary modules and libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import openai
import json
from Function_api import *
import Function_info
from config import key, systemconfig, gptmodel
import os

# Create a Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Set the OpenAI API key
api_key = os.environ.get('KEY', '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')
# openai.api_key = "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"
openai.api_key = api_key


with app.app_context():
    # Initialize the SQLAlchemy database
    db = SQLAlchemy(app)

    # Drop and create all database tables
    db.drop_all()
    db.create_all()

    # Initialize database migration
    migrate = Migrate(app, db)

    # Enable Cross-Origin Resource Sharing (CORS) for the app
    CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })

# Define a Message model for the database
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    is_user = db.Column(db.Boolean, default=True)
    button = db.Column(db.String(500))

# Set the system configuration and initial conversation history
system = systemconfig
conversation_history = [{"role": "system", "content": system}]

# opening up the chat html in the main route
@app.route('/')
def hello():
    return render_template('index.html')

# Define an endpoint to send a message
@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.json
    message_content = data.get('message')
    role = data.get('role')

    global conversation_history
    conversation_history += [{"role": role, "content": message_content}]

    # Send a message to the OpenAI chat model
    response = openai.ChatCompletion.create(
        model=gptmodel,
        messages=conversation_history,
        functions=Function_info.functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        # If the response includes a function call, execute the function
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        print(function_args)
        function_to_call = globals()[function_name]
        function_response = function_to_call(**function_args)
        conversation_history += [{"role": "function", "name": function_name, "content": function_response}]

        # Send a second message to get AI response after the function call
        second_response = openai.ChatCompletion.create(
            model=gptmodel,
            messages=conversation_history,
        )
        ai_response = second_response['choices'][0]['message']['content']
        
        # Storing User Message in the Database
        if role == "user":
            message = Message(content=message_content, is_user=True)
            db.session.add(message)

        # Storing AI Message in the Database
        conversation_history += [{"role": "assistant", "content": ai_response}]
        message = Message(content=ai_response, is_user=False)
        db.session.add(message)
        db.session.commit()
        return jsonify({"status": "Message sent successfully"})
    else:
        # If there is no function call, conversation continues
        
        # Storing User Message in the Database 
        if role == "user":
            message = Message(content=message_content, is_user=True)
            db.session.add(message)

        # Storing AI Message in the Database
        ai_response = response['choices'][0]['message']['content']
        conversation_history += [{"role": "assistant", "content": ai_response}]
        message = Message(content=ai_response, is_user=False)
        db.session.add(message)
        db.session.commit()
        return jsonify({"status": "Message sent successfully"})

# Define an endpoint to get AI messages
@app.route('/api/get_ai_messages', methods=['GET'])
def get_ai_messages():
    messages = Message.query.filter_by(is_user=False).all()
    result = [{"id": msg.id, "content": msg.content, "is_user": msg.is_user, "button": msg.button} for msg in messages]
    return jsonify({"messages": result})

# Define an endpoint to get user messages
@app.route('/api/get_user_messages', methods=['GET'])
def get_user_messages():
    messages = Message.query.filter_by(is_user=True).all()
    result = [{"id": msg.id, "content": msg.content, "is_user": msg.is_user} for msg in messages]
    return jsonify({"messages": result})

# Define an endpoint to delete all records
@app.route('/api/delete_all', methods=['DELETE'])
def delete_all():
    Message.query.delete()
    db.session.commit()
    global conversation_history
    conversation_history = [{"role": "system", "content": system}]
    return jsonify({"status": "All records deleted"})

# Run the Flask app if this file is the main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
