def ordenada(lista):
    for i in range(len(lista)-1):
        if len(lista) <= 1:
            return True
        if lista[i] > lista[i+1]:
            return False
    return True

lista = [1,2,3,4]
print(ordenada(lista))