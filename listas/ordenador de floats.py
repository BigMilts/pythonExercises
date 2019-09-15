vetor=[2.00,3.4,6.67,3.98,21.32,3.00]
def ordenador(vetor):
    elementos = 0
    while elementos < len(vetor):
        posicao = 0
        while posicao < len(vetor)-1:
            if vetor[posicao] > vetor[posicao+1]:
                temp = vetor[posicao]
                vetor[posicao] = vetor[posicao+1]
                vetor[posicao+1] = temp
                posicao+= 1
            else:
                posicao+= 1
        elementos+= 1
    return(vetor)

print(ordenador(vetor))


                    
            
