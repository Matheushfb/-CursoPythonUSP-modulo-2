#import math
def heap(lista,n):
        if n == 1:
           print(lista)
           return
        else:
            for i in range(n):
                heap(lista,n-1)
                if n % 2 != 0:
                    lista[i], lista[n - 1] = lista[n - 1], lista[i]
                else:
                    lista[0], lista[n - 1] = lista[n - 1], lista[0]
        return lista

n = 20
lista = [1,2,3,4,5,6,7,8,9,10]
heap(lista,n)