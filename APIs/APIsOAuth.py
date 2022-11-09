from email import header
from os import access
import requests

client_id = '284838e1853a9d7e1997'
client_secret = '78a6cec690acbdb335775b5a5e158161af595445'

code='577d4472250c481e49b3'
access_token = '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'

if __name__ == '__main__':

    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id' : client_id,'client_secret':client_secret, 'code':code}
    headers = {'Accept' : 'application/json'}
    response = requests.post(url , json=payload , headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        access_token  = response_json['access_token']
        print(access_token)



#https://github.com/login/oauth/authorize?client_id=284838e1853a9d7e1997&scope=repo