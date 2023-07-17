from FilaDePrioridade import FilaDePrioridade

x = FilaDePrioridade()
x.inserir(10)
x.inserir(16)
x.inserir(1)
x.inserir(6)
x.inserir(14)

print(x.itens)

x.remover()
print(x.itens)

x.remover()

print(x.itens)

x.remover()
print(x.itens)
x.remover()
print(x.itens)

