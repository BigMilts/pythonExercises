from GrafL import GrafL
from GrafM import GrafM
########################################################
def depth_search(Graf):
    if type(Graf) is not GrafL:
        Graf = Graf.back()
        Graf = GrafL(Graf)
    result = []
    _dfs(Graf,0,result)
    print(*result)
    return ''
    
def _dfs(Graf,v,visited):
    if v not in visited:
        visited += [v]
        for i in Graf.list_ajd(v):
            _dfs(Graf,i,visited)
    return visited     
########################################################

def width_search(Graf):
    if type(Graf) is not GrafL:
        Graf = Graf.back()
        Graf = GrafL(Graf)
    _bfs(Graf,0)
    return ''
    
def _bfs(Graf,vertex):
    marked = [False] * Graf.size()
    queue = []
    queue+= [vertex]
    marked[vertex] = True
    predessesor = []
    while queue:
        vert = queue.pop(0)
        predessesor +=[vert]             
        for i in Graf.list_ajd(vert):
            if not Graf.is_pondereted():
                if not marked[i]:
                    queue +=[i]
                    marked[i] = True
            else:
                if not marked[i[0]]:
                    queue += [i[0]]
                    marked[i[0]] = True
    print(*predessesor)
                   
if __name__ == '__main__':
    test2 = GrafM([(0,2,5),(0,5,3),(1,3,1),(2,0,5),(2,3,6),(3,1,1),(3,2,6),(3,5,9),(4,0,7),(5,0,3),(5,3,9)],directed = True ,pondereted = True)
    test1 =  GrafL([(0,1),(0,2),(0,3),(1,2),(2,3)])
    print(test2)
    print(depth_search(test2))
    print(width_search(test2))
