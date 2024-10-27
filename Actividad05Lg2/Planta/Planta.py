from Especie.Especie import Especie

class Planta(Especie):
    def __init__(self, nombre, capacidad_reproduccion):
        super().__init__(nombre, capacidad_reproduccion)

    def crecer(self):
        self.reproducirse()