class Node:
    def __init__(self, obj):
        self.obj = obj
        self.prox = None
        self.ante = None

    def __repr__(self): return str(self.obj)

    def __str__(self): return str(self.obj)


class Dlist:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def insert(self, value):
        objet = Node(value)
        if self.head is None and self.tail is None:
            self.head = self.tail = objet
        else:
            aux = self.head
            ante = aux.ante
            cond = True
            while cond:
                if aux.prox is not None:
                    aux = aux.prox
                    ante = aux.ante
                else:
                    cond = not cond
            aux.prox = objet
            aux.prox.ante = aux
            self.tail = objet
            self.tail.ante = aux
        self.size += 1

    def insert2(self, value):
        objet = Node(value)
        if self.head is None and self.tail is None:
            self.head = self.tail = objet
        else:
            self.tail.prox = objet
            objet.ante = self.tail
            self.tail = objet
        self.size += 1

    def __len__(self):
        return self.size

    def __contains__(self, item):
        cond = True
        aux = self.head
        while cond:
            if aux.prox is not None and aux.obj is not item:
                aux = aux.prox
            else:
                cond = not cond
        return aux.obj == item

    def __setitem__(self, key, value):
        aux = self.head
        if key <= self.size:
            for i in range(key):
                aux = aux.prox
            aux.obj = value
        else:
            raise IndexError()

    def __getitem__(self, index):
        aux = self.head
        if 1 <= index < self.__len__():
            for i in range(index):
                if aux:
                    aux = aux.prox
                else:
                    raise IndexError()
        if aux:
            return aux
        else:
            raise IndexError()

    def __str__(self):
        aux = self.head
        x = ''
        while aux is not None:
            if aux is not self.tail:
                x += str(aux.obj) + ' '
            else:
                x += str(aux.obj)
            aux = aux.prox
        return x

    def remove(self, value):
        node = Node(value)
        aux = self.head
        if self.__len__() is 1:
            self.head = self.tail = None
            self.size = 0
        else:
            ante = aux.ante
            cond = True
            while cond and aux.obj != node.obj:
                if aux.prox is not None:
                    aux = aux.prox
                else:
                    cond = not cond
            if aux.prox is None:
                if aux == node == False:
                    raise ValueError()
                else:
                    ante.prox = None
                    self.tail = ante
                    del aux
                    self.size -= 1
            else:
                ante = aux.ante
                ante.prox = aux.prox
                aux.prox.ante = ante
                del aux
                self.size -= 1


    def __repr__(self):
        return 'Dlist()'

    def insert_in_order(self, new_object):
        # implementar
        return None

    def __delitem__(self, key):
        if key > self.size:
            raise IndexError()
        else:
            pass
        return None


if __name__ == '__main__':
    lista = Dlist()
    for i in range(1, 11):
        lista.insert(i)
    lista2 = Dlist()
    for i in range(1, 11):
        lista2.insert2(i)
