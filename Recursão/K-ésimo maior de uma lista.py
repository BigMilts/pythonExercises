def maxr(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0]>lista[1]:
            lista.pop(1)
            return maxr(lista)
        else:
            lista.pop(0)
            return maxr(lista)
print(maxr([14,3,5,3,33,99,33,108,22,1,3,4]))

def k_maior(lista,k):
    aux = lista[:]
    if k ==1:
        return maxr(aux)
    else:
        remover = maxr(aux)
        lista.remove(remover)
        return k_maior(lista,k-1)

print(k_maior([14,3,5,3,33,99,33,108,22,1,3,4],3))



        
