import random
def lista_grande(n):
    lista=[0 for x in range(n)]
    for i in range(n):
        lista[i]=random.randrange(n+1)
    return lista
