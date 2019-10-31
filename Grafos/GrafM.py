import numpy as np

class GrafM:
    def __init__(self,iterable,**kwargs):
        self.__directed = kwargs.get('directed',False)
        self.__pondereted = kwargs.get('pondereted',False)
        self.__madj = np.zeros((self.__build_veterxs(iterable),self.__build_veterxs(iterable)))
        if iterable:
            return self.__build__graph(iterable) 

    def is_pondereted(self):return self.__pondereted
    def is_directed(self):return self.__directed
    def size(self):
        return len(self.__madj)
    def __build_veterxs(self,iterable):
        vertexs =[]
        for i in iterable:
            if i[0] not in vertexs:
                vertexs +=[i[0]]
            if i[1] not in vertexs:
                vertexs += [i[1]]
        return len(vertexs)
    def __getitem__(self,index):
        if index > len(self.__madj)-1:
            raise ValueError
        x = []
        for i in range(len(self.__madj[index])):
            if self.__madj[index][i] != 0:
                if self.__pondereted:
                    x += [(index,i,int(self.__madj[index][i]))]
                else: x += [(index,i)]
        return x
    def back(self):
        return self.__back()
    def __back(self):
        result = []
        for l in range(len(self.__madj)):
            for i in range(len(self.__madj[l])):
                if self.__madj[l][i] !=0:
                    if self.__pondereted: result += [(l,i,self.__madj[l][i])]
                    else:result += [(l,i)]
        return result
          
    def __repr__(self):
        x = str('GrafM('+str(self.__back())+','+'directed = '+str(self.__directed)+','+'pondereted = '+str(self.__pondereted)+')')
        return x

    def __str__(self):
        if self.__pondereted:print('-=-=-=With Weights=-=-=-')
        else:print('-=-=-=Without Weigths=-=-=-')
        x = [x for x in range(len(self.__madj))]
        print('    '+str(x[0]),end ='')
        for i in range(1,len(x)):
            if i != len(x) -1:print('  ' + str(x[i]),end ='')
            else:print('  ' + str(x[i]))
        for i in range(len(self.__madj)):
            print(str(i) +' ',self.__madj[i])    
        return ''
      
    def __build__graph(self,iterable):
        for i in iterable:
                if not self.__pondereted:
                    self.__madj[i[0]][i[1]] = 1 
                    if not self.__directed:self.__madj[i[1]][i[0]] = 1
                else:
                    self.__madj[i[0]][i[1]] = i[2]
                    if not self.__directed: self.__madj[i[1]][i[0]] = i[2]
    def is_linked(self,v1,v2):
        flag = False
        try:
            edge = self.__madj[v1][v2]
            if edge != 0: flag = not flag
        except:pass
        return flag
    def outside_grau(self,v1):
        grau = 0
        for i in self.__madj[v1]:
            if i != 0: grau += 1
        return grau
    def inside_grau(self,v1):
        grau = 0
        for i in range(len(self.__madj)):
            if self.__madj[i][v1] != 0: grau += 1
        return grau

    def list_adj(self,v1):
        return [x for x in range(len(self.__madj[v1]))if self.__madj[v1][x] != 0]
    def max_edge(self):
        if self.__pondereted:
            biggests = []
            biggest = self.__madj[0][0]
            for i in range(len(self.__madj)):
                for j in range(len(self.__madj)):
                    if self.__madj[i][j] > biggest:
                        biggest = self.__madj[i][j]
                        edge =(i,j,int(biggest))
            return edge
    def min_edge(self):
        if self.__pondereted:
            lessters = []
            edge = False
            lesster = self._aux_min()
            for i in range(len(self.__madj)):
                for j in range(len(self.__madj)):
                    if self.__madj[i][j] < lesster and self.__madj[i][j] != 0:
                        lesster = self.__madj[i][j]
                        edge = (i,j,int(lesster))
            return edge

    def _aux_min(self):
        for i in range(len(self.__madj)):
            for j in self.__madj[i]:
                if j != 0:
                    aux = j
        return aux
                
    def pass_to_ladj(self):
        from GrafL import GrafL
        x = self.__back()
        self = GrafL(x,directed = self.is_directed, pondereted = self.is_pondereted)
        return self
    def add_edge(self,v1,v2,p = 1):
        if v1 <= len(self.__madj) and v2 <= len(self.__madj):
            self.__madj[v1][v2] = p
            if not self.__directed: self.__madj[v2][v1] = p
        else:
            raise ValueError
    def remove_edge(self,v1,v2):
        if v1 <= len(self.__madj) and v2 <= len(self.__madj):
            self.__madj[v1][v2] = 0
            if not self.__directed: self.__madj[v2][v1] = 0
        else:
            raise ValueError

  

if __name__ == '__main__':
    test = GrafM([(0,1),(0,2),(0,3),(1,2),(2,3)], directed = True, pondereted = False)
    test1 =  GrafM([(0,1),(0,2),(0,3),(1,2),(2,3)])
    test2 = GrafM([(0,2,5),(0,5,3),(1,3,1),(2,0,5),(2,3,6),(3,1,1),(3,2,6),(3,5,9),(4,0,7),(5,0,3),(5,3,9)],directed = True ,pondereted = True)
    print(test2)
    #print(test2.pass_to_ladj())
    print(test2.min_edge())
        
