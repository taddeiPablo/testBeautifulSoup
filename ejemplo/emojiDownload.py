##################################################### 
### creacion de script para la descarga de emojis ###
#####################################################

from bs4 import BeautifulSoup
import urllib
import requests
import json
import io
import os
import csv

class EmojisDownload(object):
    def init (self):
        self.contents = ""
        self.beuti = None
        self.items = None
        self.agent = None
        self.path = None
        self.path_emoti = None
    def load_file(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + '/file/emo.csv'
        self.path_emoti = os.path.dirname(os.path.abspath(__file__)) # aqui el path en donde pretendo guardar los emoticones
        with open(self.path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            for row in reader:
                if row[0] != 'filename':
                    parent_dir = self.path_emoti + '\\'
                    if os.path.isdir(self.path_emoti + '\\' + row[0]) == False:
                        path = os.path.join(parent_dir, row[0]) 
                        os.mkdir(path)
                        # aqui llamamos a result_search y le pasamos la url y el path
                    else
                        # lo mismo 
    def result_search(self, search, path=""):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = search
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beauti = BeautifulSoup(self.contents, 'lxml')
        self.items = self.beauti.findAll('ul', attrs={'class': 'icons'})
        self.scrape_page_items(self.items)
    def scrape_page_items(self, ite):
        for its in ite[0].find_all('li'):
            aux = its.find_all("a", class_="view link-icon-detail")
            if len(aux) != 0:
                print(aux[0].img.attrs['data-src'])

if __name__== "__main__":
    '''#Ml = MercadoLibre()
    #Ol = Olx()
    EM = EmojisDownload()
    print("bienvenido a esta prueba")
    busqueda = input('ingrese la busqueda :')
    EM.result_search(busqueda)
    #Ml.result_search(busqueda)
    #Ol.result_search(busqueda)'''
    EM = EmojisDownload()
    EM.load_file()
    
