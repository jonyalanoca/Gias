class Moto():
    def marcha(self):
        print("Andando en dos ruedas.")
class Cuatri():
    def marcha(self):
        print("Andando en cuatro ruedas.")
class Camion():
    def marcha(self):
        print("Andando en seis ruedas.")
    
def en_marcha (auto):
    auto.marcha()
    
modelo=Camion()

en_marcha(modelo)