from Especie.Especie import Especie

class Herbivoro(Especie):
    def __init__(self, nombre, capacidad_reproduccion, capacidad_busqueda, velocidad_digestion):
        super().__init__(nombre, capacidad_reproduccion)
        self.capacidad_busqueda = capacidad_busqueda
        self.velocidad_digestion = velocidad_digestion
        self.alimento_consumido = 0

    def buscar_alimento(self, plantas):
        for planta in plantas:
            if planta.poblacion > 0:
                cantidad_a_comer = int(planta.poblacion, int(planta.poblacion * self.capacidad_busqueda))
                planta.poblacion -= cantidad_a_comer
                self.alimento_consumido += cantidad_a_comer
                break

    def morir_por_inanicion(self):
        if self.alimento_consumido == 0 and self.poblacion > 0:
            self.poblacion -= 1
