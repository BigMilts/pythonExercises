#Produto Recursivo de lista
lista = [1,2,3,4,10]
def produto(array):
    if len(array) == 1:
        return array[0]
    ele = array.pop(0)
    return ele* produto(array)
#usando o pop para resolver
def produto_slice(array):
    if array == []:
        return 1
    return array[0] *produto_slice(array[1:])
#usando o slice para para resolver
