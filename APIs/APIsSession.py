import requests

if __name__ == '__main__':
    url = 'http://api.github.com/user'

    session = requests.session()
    session.auth=('dmora@ciudaddemascotas.com','dmora2020*.')

    response = session.get(url)
    if response.ok:
        print(response.content)