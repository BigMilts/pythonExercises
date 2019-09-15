lista1=[1,2,4,5,6,7,9,10,12]
#O problema se trata de inserir um número na ordem em uma lista já ordenada
#Neste caso não podendo usar o quickSor para colocar em ordem um único número
def insertOrdered(lista,n):
    #lista =qs(lista)
    return inseri(lista,n)   
def inseri(lista,n):
    if len(lista)==1:
        if lista[0]>n:
            lista.insert(0,n)
            return lista
        else:
            lista.append(n)
            return lista             
    else:
        i = len(lista)//2
        if n<lista[i]:
            aux = lista[i:]
            lista =lista[:i]
            return inseri(lista,n) + aux
        elif n==lista[i]:
            lista.insert(i,n)
            return lista
        else:
            aux = lista[:i]
            lista = lista[i:]
            return aux + inseri(lista,n)        
def qs(lista):
    if lista == []:
        return []
    pivo = lista.pop(0)
    return qs([x for x in lista if x<=pivo]) +[pivo] + qs([y for y in lista if y>pivo])


print(insertOrdered(lista1,10))
