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
        data[0]["genderID"] = genderID

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url,json=data, headers=headers)
    if response.status_code == 200:
      return('Data posted successfully!')
    else:
      return('Error posting data')
    
def getUserIdByName(name):
    
    url = 'https://clouddevbak.asanito.app/api/asanito/Person/advancedSearch'

    with open('getUserIdByName.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data["value"] = name

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result_json = response.json()
        if "resultList" in result_json and len(result_json["resultList"]) > 0:
            id = result_json["resultList"][0]["id"]
            return id
        else:
            return 'Could not find the person'
    else:
        return 'Failed to fetch data'

def getPhoneByName(name):
    
    url = 'https://clouddevbak.asanito.app/api/asanito/Person/advancedSearch'

    with open('getUserIdByName.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data["value"] = name

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result_json = response.json()
        if "resultList" in result_json and len(result_json["resultList"]) > 0:
            id = result_json["resultList"][0]["phoneNumbers"][0]["mobile"]
            return id
        else:
            return 'Could not find the person'
    else:
        return 'Failed to fetch data'
    
def addNote(name, title, content):     
    
    url = 'https://clouddevbak.asanito.app/api/asanito/Note/add'

    with open('addNote.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data["relatedEntities"][0]["entityID"] = getUserIdByName(name)
    data["title"] = title
    data["htmlContent"] = "<p>" + content + "</p>"

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url,json=data, headers=headers)
    if response.status_code == 200:
      return('Data posted successfully!')
    else:
      return('Error posting data')
    
    
def addNegotiation(title, name=None):     
    
    url = 'https://clouddevbak.asanito.app/api/asanito/Negotiation/addNew'

    with open('addNegotiation.json', encoding='utf-8') as f:
      data = json.load(f)
    
    data["title"] = title
    if name is not None:
        data["personContectIDs"][0] = getUserIdByName(name)

    
    with open('headers.json', encoding='utf-8') as h:
      headers = json.load(h)

    response = requests.post(url,json=data, headers=headers)
    if response.status_code == 200:
      return('Data posted successfully!')
    else:
      return('Error posting data')