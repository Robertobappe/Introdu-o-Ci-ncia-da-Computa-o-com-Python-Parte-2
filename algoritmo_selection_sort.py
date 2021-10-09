def ordena(lista):
    fim=len(lista)
    for i in range(fim-1):
        posicao_minimo=i
        for j in range(i+1, fim):
            if lista[j] < lista[posicao_minimo]:
                posicao_minimo=j
        #colocando o menor elemento encontrado no começo.
        #Para isso, trocamos de lugar os elementos
        lista[i], lista[posicao_minimo]=lista[posicao_minimo], lista[i]
    return lista
