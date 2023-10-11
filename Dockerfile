# Use an appropriate Python version
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000 

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Run the Flask app
CMD ["python", "app.py"]