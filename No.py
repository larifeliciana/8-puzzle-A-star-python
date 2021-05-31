class No():
    def __init__(self, estado, pai=None, acao=None, g=0, h=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.g = g
        self.h = h

    def __str__(self):
        return str(self.estado)
