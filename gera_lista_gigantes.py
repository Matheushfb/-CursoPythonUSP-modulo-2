import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(1000))
    return lista

n = 5
print(lista_grande(10))