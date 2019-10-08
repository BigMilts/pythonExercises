#Recursão de fibonnaci
#Complexidade ed 2**n
def fibonnaci(n):
    if n == 1 or n ==0:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)
print(fibonnaci(10))
