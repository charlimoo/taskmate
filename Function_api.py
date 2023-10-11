import requests
import json

def addLeanWithNegotiation(name, lastName, mobiles, title, description):     
    
    url = 'https://clouddeveloperbak.asanito.app/api/asanito/Person/addLeanWithNegotiation'

    with open('addLeanWithNegotiation.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data["name"] = name
    data["lastName"] = lastName
    data["mobiles"] = [mobiles]
    data["negotiationAddWithPersonDto"]["title"] = title
    data["negotiationAddWithPersonDto"]["description"] = description
    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url,json=data, headers=headers)
    if response.status_code == 200:
      return('Data posted successfully!')
    else:
      return('Error posting data')