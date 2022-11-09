from email import header
import json
from os import access
import requests

if __name__ == '__main__':
    client_id = '284838e1853a9d7e1997'
    client_secret = '78a6cec690acbdb335775b5a5e158161af595445'
    code='577d4472250c481e49b3'
    access_token = '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'

    url = 'http://api.github.com/user/repos'
    payload = {'nombre':'git_api_cf_comunidad'}
    headers = {'Accept':'application/json','Authorization':'token '+access_token}

    response = requests.post(url, headers=headers,json=payload)
    
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)
