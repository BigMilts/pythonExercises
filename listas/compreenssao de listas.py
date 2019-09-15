#copreensao de listas
#[z for z in range(alguma condição)if alguma condicao]
#[y for y in lista if alguma condicao]
#exemplo 
lista1 = [1,2,3,4,5,6,7,8,9]
pares = [x for x in lista1 if x %2==0]
impares = [x for x in lista1 if x not in pares]
print(lista1,pares,impares)
