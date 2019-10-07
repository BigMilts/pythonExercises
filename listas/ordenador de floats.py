#bubble_sort
vetor=[2.00,3.4,6.67,3.98,21.32,3.00]
def ordenador(vetor):
   for i in range(1,len(vetor)-1):
     for j in range(len(vetor)-1-i):
            if vetor[j] >vetor[j+1]:troca(vetor,j,j+1)
   return vetor
def troca(A,i,j):
    A[i],A[j] = A[j],A[i]
print(ordenador(vetor))
