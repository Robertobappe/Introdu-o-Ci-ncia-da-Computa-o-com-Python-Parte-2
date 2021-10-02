def imprime_matriz(matriz):
#descobrindo as dimenssôes da matriz e armazenando
#numa lista    
    i=len(matriz)
    j=len(matriz[0])
    
    i1=0
    j1=0
    m=[]

    while i1<i:
        while j1<j:
            m.append(matriz[i1][j1])
            print(m[j1] , end=" ")
            j1+=1
        print()
        i1+=1
        j1=0
        m=[]

        if j1==j:
            print(m[j])

 
