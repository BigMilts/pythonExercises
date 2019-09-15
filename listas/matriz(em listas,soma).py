matriz1=[[1,2,3,4],[3,4,5,6],[6,78,56,-1]]
matriz2=[[34,56,34,2],[5,5,6,7],[65,54,34,2]]
resultado=[]
linha=0
while linha <len(matriz1):
    coluna=0
    resultado.append([])
    while coluna < len(matriz1[linha]):
        resultado[linha].append(matriz1[linha][coluna] + matriz2[linha][coluna])
        coluna+=1
    linha+=1


print(resultado)

        
