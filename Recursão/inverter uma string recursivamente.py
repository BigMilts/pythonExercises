def inverte(string):
    string =list(string)
    if len(string) == 1:
        return string[0]
    ele = string.pop()
    return ele + inverte(string)
print(inverte("RotaEhCorno"))
print(inverte("A grama eh amarga"))
