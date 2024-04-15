nombre=str(input("ingrese su nombre: "))
cant=len(nombre)
i=int(0)
inver=str("")
while i!=len(nombre):
    inver=inver+ nombre[cant-1]
    cant-=1   
    i+=1
print(inver)
    