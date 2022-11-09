import requests


if __name__ == '__main__':
    url = 'https://i.imgur.com/yjyncQz.jpeg'
    response = requests.get(url , stream =True) # realiza peticion sin descargar contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)
    response.close()