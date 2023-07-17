"""Fila de Prioridade Usando HEapQ do proprio python """
import heapq

h = heapq

lista = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')] # lista de tuplas com a prioridade e Nome dos individuos 

h.heapify(lista) #Ordenação de acordo com a prioridade 


print("A ordem de apresentação é:")

h.heappop(lista) # Remoção de acordo com a prioridade 

h.heappush(lista,(10,'Ana')) #Inserção de uma tupla 

for i in lista: #impressão da Fila no momento final
  print(i[0],':',i[1])