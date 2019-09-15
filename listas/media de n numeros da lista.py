val=[]
continuar=True
# x=x3[:] é o mesmo que x=x1[o:len(x1)]
while continuar==True:
    numero=input("digite um número:")
    if "0"<=numero<="9":
        int(numero)
        val.append(numero)
    elif numero=="":
        continuar=False
        
    else:
        print("por favor, digite um número valido")
       
        
soma=0
u=0
while u<len(val):
    if (val[u]==""):
        pass
    else:
        soma+=float(val[u])

    u+=1

media=soma/len(val)

print(media)
    
