########################################################
#  NUEVO EJEMPLO DE COMO ARMAR UN SCRAPY CON BEAUTIFUL
########################################################



from bs4 import BeautifulSoup
import urllib
import requests
import json

class items(object):
    url_redirec = ""
    img = ""
    price = ""
    free_interest_text= ""
    model = ""
    location = ""

class MercadoLibre(object):
    def __init__(self):
        self.contents = ""
        self.beauti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'https://listado.mercadolibre.com.ar/' + urllib.quote_plus(search)
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beauti = BeautifulSoup(self.contents, 'lxml')
        self.items = self.beauti.findAll('ol', attrs={'id': 'searchResults'})
        self.scrape_page_items(self.items)
        self.paginas = self.beauti.findAll('li',attrs={'class':'pagination__page'})
    def scrape_page_items(self, ite):
        # proceso de scrapy para mercadolibre y sus items
        for its in ite[0].find_all('li'):
            aux = its.find_all("div", class_="carousel")
            if len(aux) != 0:
                print(aux[0].ul.li.a)
                print(aux[0].ul.li.a.img)
            aux1 = its.find_all("a", class_="item__info-link")
            aux2 = its.find_all("span", class_="price__symbol")
            aux3 = its.find_all("span", class_="price__fraction")
            aux4 = its.find_all("span", class_="item-installments-text")
            aux5 = its.find_all("h2", class_="item__title")
            aux6 = its.find_all("div", class_="item__condition")
            print(aux1)
            print(aux2)
            print(aux3)
            print(aux4)
            print(aux5)
            print(aux6)
            print("\n")
    def next_to_pages(self, paginas):
        pass
#End class
class Olx(object):
    def __init__(self):
        self.contents = None
        self.beuti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'https://www.olx.com.ar/search/' + urllib.quote_plus(search)
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beuti = BeautifulSoup(self.contents, 'lxml')
        self.paginas = self.beuti.findAll('li', attrs={'class', 'items-pagination'})
        self.items = self.beuti.findAll('ul', attrs={'class', 'items-list'})
        self.scrape_page_items(self.items)
    def scrape_page_items(self, ite):
        for its in ite[0].find_all('li'):
            print(its)
            print("\n")
    def next_to_pages(self, paginas):
        pass
        

class EmojisDownload(object):
    def init (self):
        self.contents = ""
        self.beuti = None
        self.items = None
        self.agent = None
    def result_search(self, search):
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
    #Ml = MercadoLibre()
    #Ol = Olx()
    EM = EmojisDownload()
    print("bienvenido a esta prueba")
    busqueda = input('ingrese la busqueda :')
    EM.result_search(busqueda)
    #Ml.result_search(busqueda)
    #Ol.result_search(busqueda)

