def menor_nome(lista_de_nomes):
    menor = 99
    menor_temp = ""
    menor_nome = ""
    for i in lista_de_nomes:
        menor_temp = i.strip()
        if len(menor_temp) < menor:
            menor = len(menor_temp)
            menor_nome = menor_temp
        else:
            menor_temp = menor_temp
    return menor_nome.capitalize()

#def test_nome():
#    assert menor_nome(['marta','tania','     ana',]) == 'Ana'


lista_de_nomes = []
#print(menor_nome(lista_de_nomes))

