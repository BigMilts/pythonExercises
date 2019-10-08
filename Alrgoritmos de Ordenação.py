import random
def troca (A,i,j):
    temp = A[i]
    A[i]=A[j]
    A[j]=temp

#bubble_sort    
def b2(A,size):
    for i in range(size):
        for j in range(size-1):
            if A[j]>A[j+1]:troca(A,j,j+1)
                   
def selection(A,size):
    for i in range(size):
        lesster = i
        for j in range(i+1,size):
            if A[j] < A[lesster]: lesster = j
        troca(A,i,lesster)

def insertion(A,size):
    for i in range(size):
        j = i -1
        key  = A[i]
        while j>=0 and A[j]> key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
        
        

vetor = [random.randint(1,100) for x in range(20)]
print(vetor)
b2(vetor,len(vetor))
print(vetor)
print(vetor)
vetor = [random.randint(1,100) for x in range(20)]
print(vetor)
selection(vetor,len(vetor))
print(vetor)
vetor = [random.randint(1,100) for x in range(20)]
print(vetor)
insertion(vetor,len(vetor))
print(vetor)

