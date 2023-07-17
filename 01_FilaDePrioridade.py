"""Filas de prioridade são estruturas de dados abstratas em que cada dado / valor na 
fila tem uma determinada prioridade."""

#Caracteristicas Basicas de Fila de Prioridade 
"""1) Um elemento com alta prioridade é retirado da fila antes de um elemento com baixa prioridade.
   2) Se dois elementos tiverem a mesma prioridade, eles serão atendidos de acordo com sua ordem na fila."""
   
class FilaDePrioridade:
    
    def __init__(self) : # inicializaçãio da fila
        self.itens = []
        
    def filaVazia(self):
        return self.itens == []
    
    def inserir(self, item): # add itens a lista
        self.itens.append(item)
        
    def remover(self):
        max = 0
        for i in range(1,len(self.itens)):
            if self.itens[i] > self.itens[max]:
                max = i 
        item = self.itens[max]
        self.itens[max:max+1] = []
        print("{} foi removido da lista".format(item))
        return item
        
x = FilaDePrioridade()
print(x.itens)
x.inserir(2)
x.inserir(10)
x.inserir(1)
x.inserir(30)

print(x.itens)

x.remover()


x.remover()

x.remover()

print(x.itens)

