listao = [1,2,3,4,5,6,7,8,9,11,12,13]
def so_primos(array):
    if len(array)==0:
        return []
    else:
        if eh_primo(array[0]):
            head=array.pop(0)
            return [head]+so_primos(array)
        else:
            array.pop(0)
            return so_primos(array)
            
def eh_primo(n):
    cond = True
    if aux(n,n)<=2 and n is not 1:
        cond = cond
    else:
        cond = not cond
        
def aux(n,div):
    if div==1:
        if n%div==0:
            return 1                        
    else:
        if n%div==0:
            return 1 + aux(n,div-1)
        else:
            return aux(n,div-1)

print(soPrimos(listao))        
        
