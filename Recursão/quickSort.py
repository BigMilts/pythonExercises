def quick_sort(lista):
    if lista==[]:
        return []
    else:
        pivo=lista.pop(0)
        return quick_sort([x for x in lista if x<=pivo]) + [pivo] + quick_sort([y for y in lista if y>pivo])    

array=[6,768,6446,10,13,1,213123,-4,56,21]
print(quick_sort(array))
