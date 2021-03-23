##################################################### 
### creacion de script para la descarga de emojis ###
#####################################################

from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import json
import io
import os
import csv


###
# SCRIPT CREADO PARA LA DESCARGAR DE EMOTICONES DE MANERA DINAMICA
# CON ESTE SCRIPT SE LOGRO AUTOMATIZAR EL PROCESO DE DESCARGA DE EMOTICONES
# ASI SE DECLARA UNA CLASE EN PYTHON.
###
class EmojisDownload(object):
    ## metodo init donde inicializamos las variables que vamos a utilizar
    def init (self):
        self.contents = ""
        self.beuti = None
        self.items = None
        self.agent = None
        self.path = None
        self.path_emoti = None
        self.path_dir = None
        self.parent_dir = None
    ## aqui unico metodo que se llamara en el punto de inicio del script
    ## aqui lo que hacemos es a partir de un archivo tipo csv armamos la estructura de carpetas que contendra a los emoticones
    ## que se vayan decargando
    def load_file(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + '/file/emo.csv' # path en donde encontraremos al csv que utilizaremos
        self.path_emoti = os.path.dirname(os.path.abspath(__file__)) # aqui el path en donde pretendo guardar los emoticones
        # abrimos el archivo
        with open(self.path, newline='') as csvfile:
            # comenzamos a leer el archivo csv
            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
            # recorremos su contenido por filas
            for row in reader:
                # aqui ignoramos el nombre de la columna
                if row[0] != 'filename':
                    # aqui comenzamos a armar el path en donde crearemos el directorio que contendra a los emoticones
                    parent_dir = self.path_emoti + '\\'
                    # aqui evaluamos si este directorio que pretendemos crear existe o no en caso de no existir lo creamos
                    if os.path.isdir(self.path_emoti + '\\' + row[0]) == False:
                        # terminamos de crear el path para el directorio
                        self.path_dir = os.path.join(parent_dir, row[0]) 
                        # creamos el directorio en la ubicacion especificada que en este caso es la misma donde esta el script
                        os.mkdir(self.path_dir)
                        # una vez creado el directorio procedemos a obtener los datos de la web de emoticones
                        self.result_search(row[1], self.path_dir)
                    else:
                        # terminamos de crear el path para el directorio
                        self.path_dir = os.path.join(self.path_emoti + '\\', row[0])
                        # una vez creado el directorio procedemos a obtener los datos de la web de emoticones
                        self.result_search(row[1], self.path_dir)
    ## aqui en este metodo vamos a crear la logica necesaria para la obtencion
    ## de los emoticones de la web que estamos consultando
    def result_search(self, search, path_dir):
        # aqui detemminamos los tipos de navegadores que vamos a soportar
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        # aqui le pasamos la url especifica de la web de emoticones
        self.url = search
        # aqui obtenemos el contenido de la web en formato texto
        self.contents = requests.get(self.url, headers=self.agent).text #urllib.urlopen(self.url).read()
        # aqui comenzamos a procesar el contenido de la web
        self.beauti = BeautifulSoup(self.contents, 'lxml')
        # tomamos el contenido que nos importa de la web que obtuvimos anteriormente en este caso el UL que contiene los emoticones
        self.items = self.beauti.findAll('ul', attrs={'class': 'icons'})
        # aqui una vez obtenido los items que nos importan los vamos a desglosar para obtener la informacion que nos importa en este caso las imagenes
        # .png
        self.scrape_page_items(self.items, path_dir)
    ## aqui en este metodo realizaremos el trabajo final que sera obtener finalmente las imagenes .png que nos importan
    ## aqui recorreremos los items LI uno por uno y iremos tomando los .png y los guardaremos en los directorios anteriormente creados seguno correpondan
    def scrape_page_items(self, ite, filePath):
        contador = 0
        # aqui recorremos los LI de la web
        for its in ite[0].find_all('li'):
            # aqui nos importa obtener solo los tag a que sabemos que contienen los imgs a los cuales queremos llegar
            aux = its.find_all("a", class_="view link-icon-detail")
            # verificamos que no venga en 0 
            if len(aux) != 0:
                print("----------------------------------------------------------------------------------------------")
                # mostramos la url hacia el emoji a partir de la utilizacion de un atributo del tag img
                print(aux[0].img.attrs['data-src'])
                print("Items Descargados : |" + str(contador) + "|")
                print("Guardado en : " + filePath)
                print("----------------------------------------------------------------------------------------------")
                # obtenemos el nombre del emoji a partir de la utilizacion de un atributo del tag img
                title = aux[0].img.attrs['title']
                # aqui finalmente una vez obtenido el emoticon lo que realizamos es el guardado de este en la carpeta correpondiente
                urllib.request.urlretrieve(aux[0].img.attrs['data-src'], filePath + '\\' + title + '.png')
                contador = contador + 1
                os.system("cls")
## punto de entrada al script
if __name__== "__main__":
    # instanciamos un objeto tipo emoji
    EM = EmojisDownload()
    # llamamos al primer metodo que creamos.
    EM.load_file()
    print("FINALIZADA LAS DESACRGAS INGRESE CUALQUIER TECLA PARA CONTINUAR ....")
    
