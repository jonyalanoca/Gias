numero=str(input("ingrese su numero de celular: "))
cant=int(len(numero))
i=int(0)
x=int(0)
y=int(0)
e=int(0)
sin= str("")
while i<cant:
    if numero[i]=="-" and x<=y:
        x=i
    elif numero[i]=="-":
        y=i
    i+=1
while e<cant:
    if e>x and e<y:
        sin=sin + numero[e]
    e+=1
print(sin)
#print(x)
#print(y)