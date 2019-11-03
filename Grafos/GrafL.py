class GrafL:
    def __init__(self,iterable,**kwargs):
        self.__adjl = {}
        self.__directed = kwargs.get('directed',False)
        self.__pondereted = kwargs.get('pondereted',False)
        if iterable:
            return self.__build_graph(iterable)

    def is_pondereted(self):return self.__pondereted
    def is_directed(self):return self.__directed
    
    def __back(self):
        back = []
        for key,listt in self.__adjl.items():
            if not self.__pondereted:
                for j in listt:
                    back += [(key,j)]
            else:
                for j in listt:
                    back += [tuple([key]) + j]
        return back
                
                
    def __build_graph(self,iterable):
        for i in iterable:
                if i[0] not in self.__adjl.keys():
                    self.__adjl[i[0]] = []
                if i[1] not in self.__adjl.keys():
                    self.__adjl[i[1]] = []

                
                if not self.__pondereted:
                    self.__adjl[i[0]] += [i[1]]
                    if not self.__directed: self.__adjl[i[1]] += [i[0]]
                else:
                    self.__adjl[i[0]] += [(i[1],i[2])]
                    if not self.__directed: self.__adjl[i[1]] += [(i[0],i[2])]
    def __ord(self):
        x = []
        for i in self.__adjl.keys():
            x +=[i]
        x.sort()
        return x
    def __str__(self):
        if self.__pondereted:print('-=-=-=With Weights-=-=-=')
        else:print('-=-=-=Without Weights-=-=-=')
        order = self.__ord()
        for vertice in order:
            print(vertice,':' ,self.__adjl[vertice])
        return ''

    def __size(self):
        return len(self.__adjl.keys())
    def size(self):
        return self.__size()

    def __repr__(self):
        x = str('GrafL('+str(self.__back())+','+'directed = '+str(self.__directed)+','+'pondereted = '+str(self.__pondereted)+')')
        return x 

    def is_linked(self,v1,v2):
        flag = False
        for i in self.__adjl[v1]:
            if i == v2: flag = True
        return flag

    def list_ajd(self,v1):
        return self.__adjl[v1]
    def outside_grau(self,v1):
        if v1 in self.__adjl.keys():
            return len(self.__adjl[v1])
        else:raise


    def inside_grau(self,v1):
        grau = 0
        if not self.__pondereted:
            for i in self.__adjl.values():
                if v1 in i: grau+=1
        else:
            for i in self.__adjl.values():
                for j in i:
                    if j[0] == v1: grau +=1
        return grau
            
    def remove_edge(self,v1,v2):
        if v1 in self.__adjl.keys() and v2 in self.__adjl.keys():
            if self.__pondereted:
                for i in range(len(self.__adjl[v1])):
                    if self.__adjl[v1][i][0] == v2:
                        x = self.__adjl[v1].pop(i)
                        if not self.__directed:
                            self.__adjl[v2].remove((v2,x[1]))                                                                   
            else:
                if v2 in self.__adjl[v1]:self.__adjl[v1].remove(v2)
                if not self.__directed and v1 in self.__adjl[v2]:self.__adjl[v2].remove(v1)
                
                
                    

    def remove_vertex(self,v1):
        if v1 in self.__adjl.keys():
            self.__adjl[v1] = []
            if not self.__pondereted:
                for i in self.__adjl.values():
                    if v1 in i: i.remove(v1)
            else:
                for i in self.__adjl.values():
                    for j in range(len(i)):
                        if i[j][0] == v1: i.pop(j)
                                                 
    def __getitem__(self,index):
        if index in self.__adjl.keys():
            x = []
            for i in self.__adjl[index]:
                if not self.__pondereted:
                    x +=[(index,i)]
                else:
                    x += [(index,i[0],i[1])]
            return x
        raise IndexError(f'There is no vertex {index} in the Graph')
    
    def add_vertex(self,v1,v2):
        if not v1 in self.__adjl.keys() and v2 in self.__adjl.keys():
            self.__adjl[v1] = [v2]
            if not self.__directed:
                self.__adjl[v2] += [v1]
        else: raise
    def add_edge(self,v1,v2,p = None):
        if v1 in self.__adjl.keys() and  v2 in self.__adjl.keys():
            if p is None:
                self.__adjl[v1] += [v2]
                if not self.__directed:self.__adjl[v2] += [v1]
            else:
                self.__adjl[v1] += [(v2,p)]
                if not self.__directed:self.__adjl[v2] += [(v1,p)]

                
    def max_edge(self):
        if self.__pondereted:
            back = self.__back()
            edge= back[0]
            for i in back:
                if i[2] > edge[2]:
                    edge = i
                    
            return edge

    def min_edge(self):
        if self.__pondereted:
            back = self.__back()
            edge = back[0]
            for i in back:
                if i[2] < edge[2]:
                    edge = i
            return edge

    def pass_to_matrix(self):
        from GrafM import GrafM
        x = self.__back()
        self = GrafM(x,pondereted = self.__pondereted,directed = self.__directed)
        return self
                              
if __name__ == '__main__':
    test = GrafL([(0,1),(0,2),(0,3),(1,2),(2,3)],directed = True)
    test1 =  GrafL([(0,1),(0,2),(0,3),(1,2),(2,3)])
    test2 = GrafL([(0,2,5),(0,5,3),(1,3,1),(2,0,5),(2,3,6),(3,1,1),(3,2,6),(3,5,9),(4,0,7),(5,0,3),(5,3,9)],directed = True ,pondereted = True)   
    print(test)
    #test.add_vertex(4)
    #print(test2)
    #print(test2.pass_to_matrix())
    #test2.remove_edge(4,0)
    print(test2.max_edge())
    print(test2.min_edge())  
