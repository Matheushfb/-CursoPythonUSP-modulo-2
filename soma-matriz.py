def soma_matriz(m1, m2):
    m3 = []
    for i in range(len(m1)):
        s1 = m1[i]
        s2 = m2[i]
        for j in range(len(s1)):
            m3.append(s1[j]+s2[j])
    return print(m3)


#m1 = [[1,2,3],[3,2,3]]
#m2 = [[1,1,1],[1,1,1]]
#print(soma_matriz(m1,m2))