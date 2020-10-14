from bs4 import BeautifulSoup
import requests

#pedimos el url del video
print("Introduce el url del video que quieras la miniatura")
miniatura_url = input()

#Petecion a Youtube
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get(miniatura_url,headers=headers)

# Se guarda en la variable soup todo el contenido de la pagina 
soup = BeautifulSoup(r.text, 'html.parser')

# Primer filtro para quedarnos solo con los divs de watch7-content
divs = soup.find_all('div',class_='watch-main-col')
i = divs[0]

for i in divs:
    imagen = i.find('link',itemprop="thumbnailUrl")
    
imagen_url = imagen['href']
print(imagen_url)    