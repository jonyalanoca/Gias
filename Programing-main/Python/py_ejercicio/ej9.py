fecha=str(input("Ingrese su fecha de nacimiento dd/mm/aaaa: "))
print(f'Dia {fecha[:fecha.index("/")]} Mes {fecha[fecha.index("/")+1:len(fecha)-5]} Año {fecha[-4: len(fecha)]}')