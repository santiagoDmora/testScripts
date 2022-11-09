import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {

        'nombre':'David',
        'nivel':'intermedio'
    }
    headers = {'Conten-Type' : 'aplication/json' , 'access-token' : '12345'}
    response = requests.post(url , data=json.dumps(payload) , headers= headers)
    # print(response.url)

    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
        print(server)
