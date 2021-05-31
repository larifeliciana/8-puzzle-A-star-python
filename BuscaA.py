from BuscaGenerica import BuscaGenerica
from Fronteira import Fronteira
from No import No
import numpy as np

class BuscaA(BuscaGenerica):
    def __init__(self, problema):
        self.problema = problema
        self.fronteira = Fronteira(No(problema))
        self.conjunto_explorado = []

    def calcular_g(self):
        return self.no.g + 1
    
    def calcular_h(self, estado):
        objetivo = np.reshape(estado.estado_objetivo, newshape=[3,3])
        atual = np.reshape(estado.estado_atual, newshape=[3,3])
        custo = 0
        for elemento in range(1,9):
            i_objetivo = np.where(objetivo == elemento)
            i_atual = np.where(atual == elemento)
            custo += abs(i_objetivo[0] - i_atual[0]) + abs(i_objetivo[1] - i_atual[1])
        return custo

    def escolher_no(self):
        self.no = self.fronteira.remover(0)[1]
        self.conjunto_explorado.append(self.no.estado.estado_atual)

    def expandir_fronteira(self):
        #Gera todos os filhos do nó atual e adiciona na fronteira
        for acao in range(len(self.no.estado.acoes)):
            filho = self.gerar_filho(acao)
            self.adicionar_no_fronteira(filho)    
        print(self.fronteira)

    def gerar_filho(self, acao_index):
        filho_estado = type(self.problema)(self.no.estado.estado_atual.copy())
        filho_estado.acoes[acao_index]()
        filho = No(estado=filho_estado, pai=self.no,
                   g=self.calcular_g(), h=self.calcular_h(filho_estado))
        return filho

    def adicionar_no_fronteira(self, filho):
        if self.checar_conjunto_explorado(filho):
            self.fronteira.adicionar(filho.h + filho.g, filho)

    def checar_conjunto_explorado(self, no):
        item = no.estado
        if item.estado_atual and item.estado_atual not in self.conjunto_explorado:
            return True
        return False