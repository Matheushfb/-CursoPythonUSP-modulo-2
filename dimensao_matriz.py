def dimensoes(minha_matriz):
    for i in minha_matriz:
        linhas = len(minha_matriz)
    colunas = len(i)
    return print('%dX%d'%(linhas,colunas))


minha_matriz = [[1,2,3],[3,2,1]]
dimensoes(minha_matriz)