import random

class Especie:
    def __init__(self, nombre, capacidad_reproduccion):
        self.nombre = nombre
        self.capacidad_reproduccion = capacidad_reproduccion
        self.poblacion = 10

    def reproducirse(self):
        if random.random() < self.capacidad_reproduccion:
            self.poblacion += int(self.poblacion * self.capacidad_reproduccion)
                   