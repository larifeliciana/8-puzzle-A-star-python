from random import shuffle
from ProblemaGenerico import ProblemaGenerico

class Problema8Numeros(ProblemaGenerico):    
    def __init__(self, estado_inicial=[]):
        """
        Inicia o tabuleiro com o valor do estado inicial. O estado inicial pode ser
        passado como argumento ou gerado aleatoriamente.
        
        Entrada:
            estado_inicial(lista | opcional): Lista contendo o estado inicial 
            do tabuleiro.
        """
        super().__init__()
        self.estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.acoes = [self.mover_esquerda, self.mover_direita, self.mover_cima, self.mover_baixo]
        self.estado_inicial = estado_inicial or self.embaralhar()
        self.estado_atual = self.estado_inicial

    def __str__(self):
        """Gera uma string no formato do tabuleiro.

        str: Tabuleiro formatado.
        """
        tab = self.estado_atual
        return f"{tab[0:3]}\n{tab[3:6]}\n{tab[6:9]}"      

    def embaralhar(self):
        """Embaralha valores do tabuleiro para posicionar peças aleatoriamente.
        
        Saída:
            tab(list): Lista de peças do tabuleiro distribuídas aleatoriamente.
        """
        tab = self.estado_objetivo.copy()
        shuffle(tab)
        return tab

    def obter_index_vazio(self):
        return self.estado_atual.index(0)

    def trocar_posicao(self, posicao_a, posicao_b):
        """Atualiza a posição atual do tabuleiro, através da troca a posição 
        de duas peças do tabuleiro, a partir do número da posição das peças.

        Entrada:
            posicao_a (int): Posição da primeira peça a ser trocada, de 0 à 8.
            posicao_b (int): Posição da segunda peça a ser trocada, de 0 à 8.

        """
        tab_aux = self.estado_atual.copy()
        self.estado_atual[posicao_a] = tab_aux[posicao_b]
        self.estado_atual[posicao_b] = tab_aux[posicao_a]

    def mover(self, movimentos_impossiveis, complemento):
        posicao_origem = self.obter_index_vazio()
        if posicao_origem in movimentos_impossiveis:
            #print("Movimento inválido")
            return None
        self.trocar_posicao(posicao_origem, posicao_origem + complemento)

    def mover_cima(self):
        movimentos_impossiveis = [0, 1, 2]
        self.mover(movimentos_impossiveis, -3)

    def mover_baixo(self):
        movimentos_impossiveis = [6, 7, 8]
        self.mover(movimentos_impossiveis,  3)
    
    def mover_esquerda(self):
        movimentos_impossiveis = [0, 3, 6]
        self.mover(movimentos_impossiveis, -1)
    
    def mover_direita(self):
        movimentos_impossiveis = [2, 5, 8]
        self.mover(movimentos_impossiveis, 1)
