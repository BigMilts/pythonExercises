#Universidade Federal de Pernambuco- UFPE
#Centro de informática -CIn -Sistemas de Informação
#discente:Milton José Vieira Souto Maior
#login:mjvsm
#email:mjvsm@cin.ufpe.br
class Node:
    def __init__(self,value,prox=None,ante =None):
        self.__value = value
        self.__prox = prox
        self.__ante = ante
    #getters e seters
    def returnValue(self):
        return self.__value
    def returnProx(self):
        return self.__prox
    def returnAnte(self):
        return self.__ante
    def setProx(self,newNode):
        self.__prox = newNode
    def setAnte(self,newNode):
        self.__ante = newNode
    def setValue(self,newValue):
        self.__value = newValue

class ListaDuplamenteEncadeada:
    def __init__(self, objt = None):
        self.__objt = objt
        self.__head = None
        self.__size = 0
        if self.__objt is not None:
            for i in self.__objt:
                i = Node(i)
                if self.__head:
                    aux = self.__head
                    ante = aux.returnAnte()
                    while aux.returnProx():
                        ante = aux
                        aux = aux.returnProx()
                    aux.setProx(i)
                    aux.setAnte(ante)
                    self.__size+=1
                else:
                    self.__head = i
                    self.__size+=1                      
    def __str__(self):
        if self.__head is None:
            return ''
        string = ''
        aux = self.__head
        while(aux):
            if aux.returnProx() is not None:
                string +=str(aux.returnValue()) +','
            else:
                string += str(aux.returnValue())
            aux = aux.returnProx()
        return string
                                       
    def returnHead(self):
        return self.__head
    def __repr__(self):
        string = ''
        if self.__head is not None:
            aux = self.__head
            for i in range(self.__size):
                if i is self.__size - 1:
                    string+=str(aux.returnValue())
                else:
                    string+=str(aux.returnValue()) + ','
                    aux = aux.returnProx()
        return 'ListaDuplamenteEncadeada'+f'[{string}]'
     
    def __len__(self):
        return self.__size
    def __getitem__(self,index):
        aux = self.__head
        for i in range(index):
            if aux:
                aux= aux.returnProx()
            else:
                raise IndexError('Queue index out of range')
        if aux:
            return aux.returnValue()
        else:
            raise IndexError('Queue index out of range')

    def __setitem__(self,index,newValue):
        aux = self.__head
        for i in range(index):
            if aux:
                aux= aux.returnProx()
            else:
                raise IndexError('Queue index out of range')
        if aux:
            aux.setValue(newValue)
        else:
            raise IndexError('Queue index out of range')
                       
    def indice(self,value):
        aux = self.__head
        if aux is not None:
            if self.__size is 1:
                if aux.returnValue == value:
                    return 0
                else:
                    return 'ValueError'
            else:
                for i in range(self.__size):
                    if aux.returnValue() == value:
                        return i
                    aux = aux.returnProx()
                    
                        
                return 'ValueError'
              
    def anexar(self,value):
        elem = Node(value)
        aux = self.__head
        if self.__size is 0:
            self.__head = elem
            self.__size+=1
        
        elif aux is not None:
            ante = aux.returnAnte()
            while aux.returnProx():
                ante = aux
                aux = aux.returnProx()
            aux.setProx(elem)
            elem.setAnte(aux)
            self.__size+=1
        else:
            return 'ERROR'
                
    def selecionar(self,index):
        aux = self.__head
        ante = aux.returnAnte()
        if aux is not None:
            if index is 0:
                prox = aux.returnProx()
                if prox is not None:
                    prox.setAnte(None)
                y = self.__head.returnValue()
                self.__head = prox
                self.__size-=1
                return y
            
            for i in range(index):
                ante = aux
                aux = aux.returnProx()
            prox = aux.returnProx()
            ante = aux.returnAnte()
            if ante is not None:
                ante.setProx(prox)
                if prox is not None:
                    prox.setAnte(ante)
            y =aux.returnValue()
            self.__size-=1
            return y
        else:
            return 'IndexOutOfRange'
                  
    def inserir(self,index,value):
        if self.__objt is not None:
            elem = Node(value)
            aux = self.__head
            ante = aux.returnAnte()
            for i in range(index):
                ante = aux
                aux = aux.returnProx()
            prox = aux.returnProx()
            ante.setProx(elem)
            elem.setProx(aux)
            if prox is not None:
                prox.setAnte(elem)
            self.__size+=1
    def concatenar(self,lista):
        principal = []
        aux = self.__head
        cond = True
        if aux is not None:
            while cond:
                principal += [aux.returnValue()]
                if aux.returnProx() is not None:
                    principal = [aux.returnValue()]
                    aux = aux.returnProx()
                else:
                    cond = not cond
            total = (principal + lista)
            for i in lista:
                elem = Node(i)
                ante = aux.returnAnte()
                if aux is not None:
                    while aux.returnProx():
                        ante = aux
                        aux = aux.returnProx()
                    aux.setProx(elem)
                    elem.setAnte(aux)
                    self.__size+=1
            return f'l1 ={total}, l2 =[]'
                         
if __name__ == '__main__':
    test = ListaDuplamenteEncadeada()
    #test.anexar(1)
    #test.anexar(2)
    test1 = ListaDuplamenteEncadeada('algoritmos')
    test2 =ListaDuplamenteEncadeada([1,2,3,4,6])
    test2.inserir(4,5)
    test2.concatenar([7,8,9,10])                     
