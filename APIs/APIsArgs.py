import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args = {

        'nombre':'David',
        'nivel':'intermedio'
    }
    response = requests.get(url , params=args)
    print(response.url)

    if response.status_code == 200:
        # response_json = response.json()#DIC
        # origin = response_json['origin']
        # print(response.content)
        # print(origin)
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print (origin)
