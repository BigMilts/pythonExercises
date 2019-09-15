def max_recursivo(lista):
    i = len(lista) -1
    if len(lista) == 1:
        return lista[0]
    else:
        if lista [i] > lista[i-1]:
            lista.pop(i-1)
            return max_recursivo(lista)
        else:
            lista.pop(i)
            return max_recursivo(lista)

lista1 = [76,34,5,6,200,7,8,103]

print(max_recursivo(lista1))
                    
        
