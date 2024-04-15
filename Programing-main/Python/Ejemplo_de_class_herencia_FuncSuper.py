class Persona():
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    def descripcion(self):
        print(f'nombre: {self.nombre}\nedad: {self.edad}\nresidencia: {self.residencia}')
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre,edad,residencia):
        super(). __init__(nombre, edad, residencia)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print(f'antiguedad: {self.antiguedad}\nSalario: {self.salario}')

var1=Persona("jonathan","alonoca","buenos aires")
var2=Empleado(2000,"2 años","jonathan","alonoca","buenos aires")
var2.descripcion()