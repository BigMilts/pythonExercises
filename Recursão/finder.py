lista1 = [2,5,4,3,2,1,0]
lista2 = [1231,3245235,567467,765858,2423423,345346,78,7,234235,6867,6536,7568,67,45645,6,34214,3,312312342,45353456,6534674,46456,46457,4,332432,32432,432423,1,2342356,4523]
#O problema se trata de encontarr um numero numa lista de modo a dividir para conquistar
def ordena(lista):
    if lista == []:
        return []
    pivo=lista.pop(0)
    return ordena([x for x in lista if x<=pivo]) + [pivo] + ordena([y for y in lista if y>pivo])
def finder(listap,n):
    lista = listap[:]
    if len(lista)==1:
        if n==lista[0]:
            return n
        else:
            return False
    elif len(lista)==2:
        if lista[0] == n or lista[1] ==n:
            return n
        else:
            return False
    lista=ordena(lista)
    i=len(lista)//2
    if n<lista[i]:
        return finder(lista[:i],n)
    else:
        return finder(lista[i:],n)
print(finder(lista2,4))
print(lista1)
print(ordena(lista1))
        
