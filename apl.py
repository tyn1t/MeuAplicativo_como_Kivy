#import o App, Builder (gui)
#criar o aplicativo
# criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests, json

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"http://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
        
        
        


MeuAplicativo().run()
