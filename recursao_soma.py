def soma_lista(lista):
    a=len(lista)-1
        
    if a == 0:
        return lista[0]
    elif a == 1:
        return lista[0] + lista[1]

    else:
        soma=lista[0]+lista[1]
        lista.remove(lista[0])
        lista.remove(lista[0])
        soma += soma_lista(lista)
        return soma
        
    
