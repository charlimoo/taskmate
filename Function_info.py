functions = [
    {
        "name": "addLeanWithNegotiation",
        "description": "creates a profile for a person with a negotiation associated to the person in the CRM",
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
                "title": {
                    "type": "string",
                    "description": "title on the negotiation",
                },
                "description": {
                    "type": "string",
                    "description": "a short description about the negotiation",
                }
            },
            "required": ["name","lastName","mobiles" ,"title" ,"description"],
        },
    }
]