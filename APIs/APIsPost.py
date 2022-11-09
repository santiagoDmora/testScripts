import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {

        'nombre':'David',
        'nivel':'intermedio'
    }
    response = requests.post(url , data=json.dumps(payload))
    # print(response.url)

    if response.status_code == 200:
        print(response.content)
