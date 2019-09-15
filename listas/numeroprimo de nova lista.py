print("esse progama vai mostarar a os números primos existentes de 1 até o número que voce escolher")

n=int(input("digite um número inteiro:"))
i=1
numeros=[]
primos=[]
while i<=n:
    numeros.append(i)
    i+=1

quantDdivi=0
divi=1
for u in numeros:
    while divi<=u:
        if u%divi==0:
            quantDdivi+=1
        divi+=1
        
    if quantDdivi==2 and u!=1:
        primos.append(numero[u])
   


print(primos)

    
            
