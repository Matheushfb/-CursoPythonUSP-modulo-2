def busca(lista,elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False

#x=4
#lista = [1,2,3,4,5,6]
#print(busca([1,2,3,4,5,6],4))