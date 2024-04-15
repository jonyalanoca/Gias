frase=str(input("Introduzca una frase: "))
vocal=str(input("introduzca una vocal: "))
i=int(0)
frase_m=str("")
while i< len(frase):
    if frase[i]== vocal:
        frase_m += frase[i].upper()    
    else:
        frase_m += frase[i]       
    i+=1
print(frase_m)