from copy import copy
from No import No
from Fronteira import Fronteira

class BuscaAbstrata():
    def __init__(self, problema):
        pass

    def buscar(self):
        raise Exception("Não implementado")

    def adicionar_no_fronteira(self, filho):
        raise Exception("Não implementado")    

    def checar_conjunto_explorado(self, no):
        raise Exception("Não implementado")

    def obter_solucao(self):
        raise Exception("Não implementado")

    def expandir_fronteira(self):
        raise Exception("Não implementado")

    def gerar_filho(self):
        raise Exception("Não implementado")

    def calcular_custo(self, no):
        raise Exception("Não implementado")

    def escolher_no(self):
        raise Exception("Não implementado")

