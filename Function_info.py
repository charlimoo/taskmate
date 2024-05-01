functions = [
    {
        "name": "AddLeanWithApi",
        "description": "creates a profile for a person in the CRM",
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
                    "description": "gender of the person, male is 1 and female is 2, unknown is 3. guess the gender based on the given name",
                }
            },
            "required": ["name","lastName","mobiles"],
        },
    }
]