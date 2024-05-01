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
    }
]