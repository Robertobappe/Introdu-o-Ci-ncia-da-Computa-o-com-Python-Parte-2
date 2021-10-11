def insertion_sort(lista):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(lista)):
  
        key = lista[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < lista[j] :
                lista[j+1] = lista[j]
                j -= 1
        lista[j+1] = key
    return lista
