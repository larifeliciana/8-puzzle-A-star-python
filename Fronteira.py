class Fronteira():
    def __init__(self, raiz):
        self.nos = [(0, raiz)] #(custo, no)

    def ordernar_fronteira(self):
        self.nos = sorted(self.nos, key=lambda x: x[0])
    
    def adicionar(self, custo_final, no):
        self.nos.append((custo_final, no))
        self.ordernar_fronteira()

    def remover(self, index):
        return self.nos.pop(index)

    def __str__(self):
        string = "Fronteira: \n"
        for elemento in self.nos:
            string += str(elemento[0]) + "\n" + str(elemento[1]) + "\n\n"
        return string
