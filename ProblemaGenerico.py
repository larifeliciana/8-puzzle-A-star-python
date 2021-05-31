class ProblemaGenerico():
    def __init__(self, estado_objetivo=None, acoes=None, estado_inicial=None):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acoes = acoes
        self.estado_atual = estado_inicial

    def __str__(self):
        return str(self.estado_atual)
    
    def testar_objetivo(self):
        return self.estado_atual == self.estado_objetivo
