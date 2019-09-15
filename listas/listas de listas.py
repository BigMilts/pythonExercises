
#maior entre as listas
def maiorEntreAsListas(listaDeListas):
    maiores = []
    for lista in listaDeListas:
        maiores.append(maior(lista))
    return maior(maiores)   



#maior elemento de uma lista
def maior(lista):
    maior=lista[0]
    for elemento in lista:
        if elemento >maior:
            maior=elemento
    return(maior)        


"""

def maiorEntreASlistasNoob(listasDelistas):
    todos= []
    for lista in listaDeListas:
        todos = todos +çista

    return maior(todos)
    
        """

"""
