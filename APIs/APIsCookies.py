import re
import requests

if __name__ == '__main__':

        url = 'https://httpbin.org/#/Cookies'
        cookies = {'my-cookie':'true'}
        response = requests.get(url, cookies= cookies)

        if response.ok:
            cookies = response.cookies
            print(cookies)
            print(response.content)