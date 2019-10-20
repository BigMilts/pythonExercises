#Universidade Federal de Pernambuco- UFPE
#Centro de informática -CIn -Sistemas de Informação
#discente:Milton José Vieira Souto Maior
#login:mjvsm
#email:mjvsm@cin.ufpe.br
class Node:
    def __init__(self,value):
        self.__value = value
        self.__prox = None
    def returnValue(self):
        return self.__value
    def returnProx(self):
        return self.__prox
    def setProx(self,newNode):
        self.__prox = newNode

class Fila:
    def __init__(self,objt =None):
        self.__objt = objt
        self.__head = None
        self.__size = 0
        if self.__objt is not None:
            for i in self.__objt:
                i = Node(i)
                if self.__head:
                    aux = self.__head
                    while(aux.returnProx()):
                        aux = aux.returnProx()
                    aux.setProx(i)
                    self.__size += 1
                else:
                    self.__head = i
                    self.__size += 1
    def __len__(self):
        return self.__size
    def __str__(self):
        if self.__head is None:
            return ''
        string = ''
        aux = self.__head
        while(aux):
            if aux.returnProx() != None:
                string +=str(aux.returnValue()) +','
            else:
                string += str(aux.returnValue())
            aux = aux.returnProx()
        return string
    def __repr__(self):
        string = ''
        if self.__head != None:
            aux = self.__head
            while(aux):
                string += str(aux.returnValue())
                aux = aux.returnProx()
        return 'Fila' + str(list(string))
            
    def enqueue(self,value):
        value = Node(value)
        if self.__head:
            aux = self.__head
            while(aux.returnProx()):
                aux = aux.returnProx()
            aux.setProx(value)
            self.__size += 1
        else:
            self.__head = value
            self.__size += 1
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
    def dequeue(self):
        if self.__head is not None:
            aux1 = self.__head.returnProx()
            aux2 = aux1.returnProx()
            x = self.__head.returnValue()
            self.__head = aux1
            self.__head.setProx(aux2)
            return x
        else:
            raise IndexError("The Queue is empty")
        
        
       
class Stack(Fila):
    def __init__(self,objt = None):
        super().__init__(objt)
        self.__objt = objt
        self.__head = None
        self.__size = 0
        if self.__objt is not None:
            for i in self.__objt:
                i = Node(i)
                if self.__head:
                    aux = self.__head
                    while(aux.returnProx()):
                        aux = aux.returnProx()
                    aux.setProx(i)
                    self.__size += 1
                else:
                    self.__head = i
                    self.__size += 1
     
    def enqueue(self):
        return None
    def push(self,value):
        elem = Node(value)
        aux = self.__head
        if aux.returnProx() is None:
            aux.setProx(elem) 
        else:
            while aux.returnProx() is not None:
                aux = aux.returnProx()
            aux.setProx(elem)
            

    def __repr__(self):
        string = ''
        if self.__head != None:
            aux = self.__head
            while(aux):
                string += str(aux.returnValue())
                aux = aux.returnProx()
        return 'Stack' + str(list(string))
    def dequeue(self):
        return None
    def __getitem__(self,index):
            return None
    def pop(self):
        if self.__size >0:
            aux= self.__head.returnProx()
            ante = self.__head
            cond = True
            while(aux and cond):
                if aux.returnProx() == None:
                  ante.setProx(None)
                  cond = False
                else:
                    ante = aux
                    aux = aux.returnProx()
            elem = aux.returnValue()
            self.__size -=1
            return elem
                
                    
        else:
            raise IndexError('The Stack is out Of range')
    def showTop(self):
        aux = self.__head
        while aux.returnProx():
            aux = aux.returnProx()
        return aux.returnValue()
                
    
        
if __name__ == '__main__':
    test = Fila()
    test.enqueue(2)
    test.enqueue(4)
    test.enqueue(5)
    sil = Fila('abc')
    pil = Stack('123')
    pil.pop()
    pil.push(3)
