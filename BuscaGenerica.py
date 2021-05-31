from copy import copy
from No import No
from Fronteira import Fronteira
from BuscaAbstrata import BuscaAbstrata

class BuscaGenerica(BuscaAbstrata):
    def __init__(self, problema):
        self.problema = problema
        self.fronteira = Fronteira(No(problema))
        
    def buscar(self):
        rodada = 1
        while True:
            print(f"Rodada {rodada}\n\n")
            rodada += 1
            
            #Checa se ainda há elementos na fronteira
            if not self.fronteira:
                raise Exception("Solução não encontrada")

            #Seleciona da fronteira o nó a ser analisado atualizando a fronteira
            self.escolher_no()
            print("Nó Atual: \n")
            print(self.no.estado)

            #Testa função objetivo
            if self.no.estado.testar_objetivo():
                print("\nSolução Encontrada.")
                self.obter_solucao()
                return
               
            else:
                print("\nNó não é a solução, expandindo fronteira...\n\n")
                self.expandir_fronteira()

    def obter_solucao(self):
        print("\nSolução Final:")
        solucao = []
        n_movimentos = self.no.g
        while self.no.pai:
            solucao.insert(0, self.no)
            self.no = self.no.pai
            
        for no in solucao:
            print(no)
            print("\n↓\n")
        
        print(f"Número de Movimentos: {n_movimentos}\n")
        print("EXECUÇÃO FINALIZADA")