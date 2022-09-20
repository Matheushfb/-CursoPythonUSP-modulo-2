def maiusculas(frase):
    letras = []
    for i in frase:
        if ord(i) >= 65 and ord(i) <= 90: # Verifica se o valor da tabela ASCII esta no range valido.
            letras.append(i)    # Caso seja valido ele armazena a variável no array
    return letras

frase = ""
