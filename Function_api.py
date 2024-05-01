import requests
import json


def AddLeanWithApi(name, lastName, mobiles, genderID=None):     
    
    url = 'https://clouddevbak.asanito.app/api/asanito/Person/AddLeanWithApi'

    with open('AddLeanWithApi.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data[0]["name"] = name
    data[0]["lastName"] = lastName
    data[0]["mobiles"] = [mobiles]
    if genderID is not None:
        data[0]["genderID"] = [genderID]

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url,json=data, headers=headers)
    if response.status_code == 200:
      return('Data posted successfully!')
    else:
      return('Error posting data')
    
