lista=[]
print("digite -1 para parar a sequencia")
n = 0
while n!=-1:
    n=int(input("digite um número para ser adicionado na sequencia: "))
    lista.append(n)
elementos=0
print(lista)
while elementos < len(lista):
    posicao=0
    while posicao < len(lista)-1:
        if lista[posicao]>lista[posicao+1]:
            temp =lista[posicao]
            lista[posicao]=lista[posicao+1]
            lista[posicao+1]=temp
            posicao+=1
        else:
            posicao+=1
    elementos+=1
print(lista)                  
