numeros = [4,7,21,34,28]
mul_sete = []
i=0
while i<len(numeros):
    if numeros[i]%7==0:
        mul_sete.append(numeros[i])
        i+=1
    else:
        i+=1
       
    
print(mul_sete)




