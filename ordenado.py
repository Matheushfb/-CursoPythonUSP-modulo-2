def ordenada(lista):
    count = 0
    for i in range(len(lista)):
        if len(lista) <= 1:
            return True
        if lista[i] < lista[i+1]:
            count = count + 1
            if count == len(lista) - 1:
                return True
        else:
            return False

#lista = [1]
#print(ordenada(lista))