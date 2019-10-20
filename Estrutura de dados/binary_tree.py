#Universidade Federal de Pernambuco- UFPE
#Centro de informática -CIn -Sistemas de Informação
#discente:Milton José Vieira Souto Maior
#login:mjvsm
#email:mjvsm@cin.ufpe.br
class Node:
    def __init__(self,key,value):
        self.key = key
        self.right = None
        self.left = None
        self.value = value
        self.parent = None
    def __str__(self):
        if self.key:
            return str(self.key)
    def __repr__(self):
        if self.key:
            return str(self.key)
    def __lt__(self,new_node):
        if type(new_node) is Node :return self.value < new_node.value
        raise TypeError('The object is not a Node')
    def __gt__(self,new_node):
        if type(new_node) is Node :return self.value > new_node.value
        raise TypeError('The object is not a Node')
    def __le__(self,new_node):
        if type(new_node) is Node :return self.value <= new_node.value
        raise TypeError('The object is not a Node')
    def __ge__(self,new_node):
        if type(new_node) is Node :return self.value >= new_node.value
        raise TypeError('The object is not a Node')
    def __eq__(self,new_node):
        if  type(new_node) is Node :return self.value == new_node.value
        raise TypeError('The object is not a Node')
    def __ne__(self,new_node):
        if type(new_node) is Node :return self.value != new_node.value
        raise TypeError('The object is not a Node')
    def __dict__(self):
        pass
#############################################################################        
class Binary_tree:
    
    def __init__(self,objecty = None):
        self.root = None
        if objecty:
            for i in objecty:
                self.insert(i)
        
        
    def __bool__(self):
        self.empty = False
        if self.root is not None:
            self.empty = not self.empty
        return self.empty
    
    def __print_inorder(self,node,dic = {}):
        if node is not None:
            self.__print_inorder(node.left,dic)
            dic[node.key] = node.value
            self.__print_inorder(node.right,dic)
        return  'Tree traveled inorder ' + str(dic) 
    
    def __str__(self):
        return self.__print_inorder(self.root,{})
    def __print_preorder(self,node,dic = {}):
        if node is not None:
            dic[node.key] = node.value
            self.__print_preorder(node.left,dic)
            self.__print_preorder(node.right,dic)
        return 'Tree traveled in preorder '  + str(dic) 
    
    def __repr__(self):
        return self.__print_preorder(self.root,{})

    def __getitem__(self,key):
       x = self.__search(key)
       return x.value
    def get(self,key):
        return self.__search(key)
    def __search(self,key):
        aux = self.root
        while aux:
            if key == aux.key:
                return aux
            elif key > aux.key:
                aux = aux.right
            else:
                aux = aux.left
        raise IndexError('This key is not in the tree')
    
    def __setitem__(self,key,value):
        node = self.__search(key)
        node.value = value
        
    def __contains__(self,key):
        flag = True
        try:self.__getitem__(key)
        except:flag = not flag
        return flag
    
    def __print_posorder(self,node,dic = {}):
        if node:
            self.__print_posorder(node.left,dic)
            self.__print_posorder(node.right,dic)
            dic[node.key] = node.value
        return 'Tree in posorder ' + str(dic) 
    def print_posorder(self):
        return self.__print_posorder(self.root)
        
    #def __next__(self):
        #return self.print_posorder(self.root)
       
    #def __iter__(self):
        #return self

    def __posorder(self,node,array = []):
        if node is not None:
            array = self.__posorder(node.left,array)
            array = self.__posorder(node.right,array)
            array +=[node.key]
        return array

    def reiniciar(self):
        lista = self.__posorder(self.root)
        for i in lista:
            try:
                self.__delitem__(i)
            except:
                pass
            
        return self
        
        

    def __get_max(self,node):
        aux = node
        while aux.right:
            aux = aux.right
        return aux
    def __get_min(self,node):
        aux = node
        while aux.left:
            aux = aux.left
        return aux
    def tree_mininum(self):
        if self.root:
            return self.__get_min(self.root).key
        raise ValueError('The tree is empty')
    def tree_maximum(self):
        if self.root:
            return self.__get_max(self.root).key
        raise ValueError('The tree is empty')
    
    def insert(self,pair):
        #pair[0] == Key
        #pair[1] == Value
        if self.__contains__(pair[0]):return 'The Key is arealdy in the tree'
        new_node = Node(pair[0],pair[1])
        if self.root is None:
            self.root = new_node 
        else:
            aux = self.root
            cond = True
            while cond:
                if pair[0] > aux.key:
                    if aux.right:aux = aux.right
                    else:cond = not cond
                elif pair[0] < aux.key:
                    if aux.left:aux = aux.left
                    else:cond = not cond
                else:
                    cond = not cond
                    #Send a error, because the key is already in the tree
            if new_node.key > aux.key:aux.right = new_node
            elif new_node.key < aux.key:aux.left = new_node
            new_node.parent = aux
    
    def sucessor(self,node):
        if node.right:
            return self.__get_min(node.right)
        father = node.parent
        while father:
            if node is not father.right:
                return father
            node = father
            father = father.parent
    
    def predecessor(self,node):
        if node.left:
            return self.__get_max(node.left)
        father = node.parent
        while father:
            if node is not father.left:
                return father
            node = father
            father = father.parent     
        
    def __delitem__(self,key):
        node = self.__search(key)
        #print(node)
        if node.right is None and node.left is not None:
            #print(1)
            node.key,node.value = node.left.key,node.left.value
            node.left = None
        elif node.left is None and node.right is not None:
            node.key,node.value = node.right.key,node.right.value
            node.right = None
            #print(2)
        elif node.right is None and node.left is None:
            father = node.parent
            if node == self.root:
                self.root = None
            else:
                if node.key > father.key:
                    father.right = None
                elif node.key < father.key:
                    father.left = None
                del node    
        else:
            sucessor = self.sucessor(node)
            dad_sucessor = sucessor.parent
            dad_sucessor.right = sucessor.left
            node.value,node.key = sucessor.value,sucessor.key
            del sucessor
    def __aux(self,array,node,case):
        if node is not None:
            if case is 1:
                array += [node.key]
                case = 1
            else:
                array += [node.value]
                case = 2
            array = self.__aux(array,node.left,case)
            array = self.__aux(array,node.right,case)
        return array
                  
    
    def keys(self):
        a_keys = []
        a_keys = self.__aux(a_keys,self.root,1)
        return a_keys
    def values(self):
        a_values = []
        a_values =self.__aux(a_values,self.root,2)
        return a_values


                        
if __name__ == '__main__':
    teste = Binary_tree([(15,155),(6,66),(18,1818),(3,33),(7,77),(13,1313),(2,22),(4,44),(9,99),(17,1717),(20,2020),(22,2222)])
    t2 = Binary_tree()
    test2 =[(10,10),(13,13),(7,7),(5,5),(8,8),(12,12),(14,14),(14,14)]
    #inserir nos na arvore pelo método Insert()
    for i in test2:
        t2.insert(i)
    del teste[13]
    cavi = Binary_tree([(50,50), (49,49), (35, 35), (38, 38), (36, 36), (37, 37), (43, 43), (40, 40), (41, 41), (39, 39), (46, 46), (30, 30), (33, 33), (31, 31), (25, 25), (28, 28),
                               (54, 54), (53, 53), (51, 51), (52, 52), (65, 65), (60, 60), (63, 63), (61, 61), (62, 62), (58, 58), (59, 59), (56, 56), (70, 70), (68, 68), (69, 69) ])    
