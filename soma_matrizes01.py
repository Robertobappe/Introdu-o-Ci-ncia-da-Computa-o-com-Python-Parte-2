#descobrindo a dimensão das matrizes e armazenando
#numa lista
def dimensoes(m1,m2):
    i1=len(m1)
    j1=len(m1[0])
    i2=len(m2)
    j2=len(m2[0])
    m=[i1,j1,i2,j2]
    return m

#criando uma matriz de n_linhas, n_colunas com valor
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = []
    i=0
    j=0
    while i<n_linhas:
        linha = []
        while j <n_colunas:
            linha.append(valor)
            j+=1
        matriz.append(linha)
        i+=1
        j=0
    return matriz

def soma_matrizes(m1,m2):
    m=dimensoes(m1,m2)
#verificando se as matrizes tem as mesmas dimensôes
    if m[0]==m[2] and m[1]==m[3]:
        n=crie_matriz(m[0], m[1], 0)
        a=0
        b=0
#efetuando a soma das matrizes
        for a in range(m[1]-1):
            for b in range(m[0]+1):
                n[a][b]=m1[a][b]+m2[a][b]
        return n
    else:
        return False

