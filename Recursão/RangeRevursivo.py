def rangeRecursivo(inicio,final,passo):
    if inicio==final:
        return []
    elif inicio<final:
        if passo>0:
            if passo<final:
                x=inicio+passo
                return [inicio] + rangeRecursivo(x,final,passo)
            else:
                return [0]
        else:
            return []
    else:
        if passo<0:
            if inicio>final:
                x = inicio + passo
                return  [inicio]+ rangeRecursivo(x,final,passo)
            else:
                return []
        else:
            return [0]

print(rangeRecursivo(-2,6,2))
print(rangeRecursivo(1,20,1))
print(rangeRecursivo(0,1,5))
print(rangeRecursivo(20,1,-1))
print(rangeRecursivo(24,3,-2))
