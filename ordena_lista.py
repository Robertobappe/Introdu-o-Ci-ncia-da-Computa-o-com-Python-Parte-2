def ordenada(lista):
    a=True
    b=True
    for i in range(len(lista)-1):
        posicao_minimo=i
        for j in range(i+1, len(lista)):
            if lista[j]<lista[posicao_minimo]:
                a=False
                return False
            else:
                b=True
    if a == True and b == True:
        return True
