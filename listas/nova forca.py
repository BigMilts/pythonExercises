secreta =(input("digite a palavra secreta: "))
linha = 50
letras = []
tentativas = 6
secreta1 = list(secreta)
aux = 0
while linha >0:
    print("")
    linha-=1

for i in secreta1:
    letras.append("-")

acertou = False

while acertou == False and tentativas != 0:
    letra = input("digite uma letra:")
    if len(letra) >1:
        if list(letra) != list(secreta):
            tentativas = 0
            print("LAMENTO VOCÊ ERROU, E DESPERDISSOU SUAS CHANCES")
        elif list(letra) == list(secreta):
            tentativas = 0   
            print("parabéns, você ganhou o jogo")
    elif len(letra) == 1:        
        for i in range(0,len(secreta1)):
            if letra == secreta[i]:
                letras[i] = letra
                acertou = True
                
        print(letras)
        if acertou == False:
            tentativas-=1
            

    for i in letras:
        if i == "-":
            acertou = False                   
                   
if acertou == True:
    print("voce ganhou o jogo, parabéns")
    
if tentativas == 0:
    acertou = True
    print("você perdeu todas as tentativas")
    print("A palavra era:",secreta)
               
