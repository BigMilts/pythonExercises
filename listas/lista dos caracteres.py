palavras=["CALU$%#$","SIRIC4SCUD&","2321@#%%#%%&%#%@"]
caracter=[]
i=""

for p in palavras:
    for j in p:
        if "!"<=j<="/" or ":"<=j<="@" or "["<=j<="`" or "{"<=j>="~":
            i+=j
    caracter.append(i)
            


print(caracter)
print(i)           
