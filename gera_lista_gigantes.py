import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(n))
    return lista
