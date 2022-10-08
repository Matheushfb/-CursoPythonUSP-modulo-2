def soma_matrizes(m1, m2):
    m3 = []
    linha = []
    if len(m1) != len(m2):
        return 0
    else:
        for i in range(len(m2)):
                s = m1[i]
                s2 = m2[i]
                for j in range(len(s)):
                    linha.append(s[j] + s2[j])
                m3.append(linha)
                linha = []
    return m3

def test_soma():
    assert soma_matrizes([[1,2,3],[1,2,3]],[[3,2,1],[3,2,1]]) == [[4,4,4],[4,4,4]]

def test_matrizes_dif():
    assert soma_matrizes([[1,2,3],[1,2,3]],[[3,2,1]]) == 0

def teste_matriz_unidimensional():
    assert soma_matrizes([[1]], [[3]]) == [[4]]


m1 = [[1,2,3],[1,2,3]]
m2 = [[3,2,1],[3,2,1]]
#m1 = [[2],[1]]
#m2 = [[5],[1]]
print(soma_matrizes(m1,m2))