from Especie.Especie import Especie

class Carnivoro(Especie):
    def __init__(self, nombre, capacidad_reproduccion, capacidad_busqueda, tasa_efectividad):
        super().__init__(nombre, capacidad_reproduccion)
        self.capacidad_busqueda = capacidad_busqueda
        self.tasa_efectividad = tasa_efectividad
        self.alimento_consumido = 0

    def buscar_alimento(self, herbivoros):
        for herbivoro in herbivoros:
            if herbivoro.poblacion > 0:
                cantidad_a_comer = int(herbivoro.poblacion,int(herbivoro.poblacion * (self.capacidad_busqueda * self.tasa_efectividad)))
                herbivoro.poblacion -= cantidad_a_comer
                self.alimento_consumido += cantidad_a_comer
                break

    def morir_por_inanicion(self):
        if self.alimento_consumido == 0 and self.poblacion > 0:
            self.poblacion -= 1