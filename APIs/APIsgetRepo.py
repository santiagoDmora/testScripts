from email import header
from os import access
import requests

client_id = '284838e1853a9d7e1997'
client_secret = '78a6cec690acbdb335775b5a5e158161af595445'

code='577d4472250c481e49b3'
access_token = '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'

if __name__ == '__main__':
    url = 'http://api.github.com/user/repos'
    header = {'Authorization': 'token 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'}

    response = requests.get(url,headers=header)
    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)

#https://github.com/login/oauth/authorize?client_id=284838e1853a9d7e1997&scope=repo