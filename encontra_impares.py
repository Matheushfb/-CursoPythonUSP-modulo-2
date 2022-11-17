def encontra_impares(lista, impar=[]): #Parametro impar sendo uma lista com o valor igual não atrapalha a chamada da função, pelo fato de usar o simbolo = não tornar o parametro obrigatorio
    if len(lista) <= 1: # Verificação caso a lista possua um elemento  ou nenhum elemento
        if  lista[0]%2 != 0: #Caso a condição acima passe ele verifica se o numero é impar.
            impar.extend(lista[:1]) # Se a o numero for impar na condição acima ele adiciona esse unico elemento na lista de números impares.
        return impar #Retorna o único ou o conjunto de numeros impares
    else: # Caso a lista seja maior entro nesse elsee vai extendendo a lista de impar e chamando a função recursivamente
        if lista[0]%2 != 0:
            impar.extend(lista[:1])
            return encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])



#lista=[4]
#print(encontra_impares(lista))