def busca(lista,x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return False

#lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#x = 100
#print(busca(lista,x))