def soma_matrizes(m1, m2):
    m3 = []
    linha = []
    if len(m1) != len(m2):
        return False
    else:
        for i in range(len(m2)):
                s = m1[i]
                s2 = m2[i]
                for j in range(len(s)):
                    linha.append(s[j] + s2[j])
                m3.append(linha)
                linha = []
    return m3


m1 = []
m2 = []
#m1 = [[2],[1]]
#m2 = [[5],[1]]
soma_matrizes(m1,m2)