gptmodel = "gpt-3.5-turbo-0613"

systemconfig = """
You are a helpful assistant at آسانیتو CRM.
you talk in Persian unless you are asked to talk in another language.
you do not provide links in your responses.
you dont talk about anything outside the asanito CRM.
dont ask follow up questions.
dont offer additional help.
keep your conversation extremely short and friendly.
talk in a witty tune.
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
    },
    {
        "name": "getPhoneByName",
        "description": "finds the phone number of a person",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to find his/her phone number"
                    }
            },
            "required": ["name"],
        },
    },
    {
        "name": "addNegotiation",
        "description": "creates a Negotiation. can be for a person in the asanito CRM but the person is optional.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "title of negotiation"
                },
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to create a negotiation for if asked to",
                }
            },
            "required": ["title"],
        },
    },
    {
        "name": "addCall",
        "description": "creates a call log for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a call log in his/her profile"
                },
                "content": {
                    "type": "string",
                    "description": "the note/title that the user wants to add to the call log",
                }
            },
            "required": ["name","content"]
        }
    },
    {
        "name": "newMeeting",
        "description": "creates a meeting for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a meeting in his/her profile"
                },
                "title": {
                    "type": "string",
                    "description": "summarize the content into a short title for the meeting"
                },
                "content": {
                    "type": "string",
                    "description": "the note/title that the user wants to add to the meeting",
                }
            },
            "required": ["name","content", "title"]
        }
    }
]