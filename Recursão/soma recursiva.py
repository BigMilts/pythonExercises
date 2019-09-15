#somar números de n até 1
#considerando que n seja >=1
def soma(n):
    if n == 1:
        return n
    return soma(n-1) +n
print(soma(4))
