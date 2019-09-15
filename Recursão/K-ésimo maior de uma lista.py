def maxR(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0]>lista[1]:
            lista.pop(1)
            return maxR(lista)
        else:
            lista.pop(0)
            return maxR(lista)



print(maxR([14,3,5,3,33,99,33,108,22,1,3,4]))

def kMaior(lista,k):
    aux = lista[:]
    if k ==1:
        return maxR(aux)
    else:
        remover = maxR(aux)
        lista.remove(remover)
        return kMaior(lista,k-1)


print(kMaior([14,3,5,3,33,99,33,108,22,1,3,4],3))



        
