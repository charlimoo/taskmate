gptmodel = "gpt-3.5-turbo-0613"

systemconfig = """
You are a helpful assistant at آسانیتو CRM.
you talk in Persian unless you are asked to talk in another language.
you do not provide links in your responses.
you dont talk about anything outside the asanito CRM.
"""

functions = [
    {
        "name": "AddLeanWithApi",
        "description": "creates a profile for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "First name of the person"
                },
                "lastName": {
                    "type": "string",
                    "description": "Last name of the person",
                },
                "mobiles": {
                    "type": "string",
                    "description": "Phone number of the person",
                },
                "genderID": {
                    "type": "number",
                    "description": "gender of the person. write 1 for male, 2 for female, and 3 when the gender is unknown. try guessing the gender based on the given name by user",
                }
            },
            "required": ["name","lastName","mobiles"],
        },
    },
    {
        "name": "addNote",
        "description": "creates a note for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a note in his/her profile"
                },
                "title": {
                    "type": "string",
                    "description": "summarize the content into a short title for the note",
                },
                "content": {
                    "type": "string",
                    "description": "the note that the user wants to add to a person's profile",
                }
            },
            "required": ["name","title","content"],
        },
    }
]