from Planta.Planta import Planta
from Herviboro.Herbivoro import Herbivoro
from Carnivoro.Carnivoro import Carnivoro
from Especie.Especie import Especie
import json
import random

class Ecosistema:
    def __init__(self):
        self.plantas = []
        self.herbivoros = []
        self.carnivoros = []

    def agregar_especie(self, especie):
        if isinstance(especie, Planta):
            self.plantas.append(especie)
        elif isinstance(especie, Herbivoro):
            self.herbivoros.append(especie)
        elif isinstance(especie, Carnivoro):
            self.carnivoros.append(especie)

    def simular_dia(self):

        print("Iniciando un nuevo día...")
        # Las plantas crecen primero.
        for planta in self.plantas:
            planta.crecer()

        # Los herbívoros buscan alimento.
        for herbivoro in sorted(self.herbivoros,
                                 key=lambda h: h.capacidad_busqueda,
                                 reverse=True):  
            herbivoro.buscar_alimento(self.plantas)

        # Los carnívoros buscan alimento.
        for carnivoro in sorted(self.carnivoros,
                                key=lambda c: c.capacidad_busqueda * c.tasa_efectividad,
                                reverse=True):  
            carnivoro.buscar_alimento(self.herbivoros)

        # Mortalidad por inanición.
        for herbivoro in self.herbivoros:
            herbivoro.morir_por_inanicion()

        for carnivoro in self.carnivoros:
            carnivoro.morir_por_inanicion()

        # Reproducción.
        for planta in self.plantas:
            planta.reproducirse()

        for herbivoro in [h for h in self.herbivoros if h.alimento_consumido > 0]:
            herbivoro.reproducirse()

        for carnivoro in [c for c in self.carnivoros if c.alimento_consumido > 0]:
            carnivoro.reproducirse()

    def mostrar_estadisticas(self):
        print("\nEstadísticas del ecosistema:")
        for planta in self.plantas:
         print(f"{planta.nombre} (planta): {planta.poblacion} individuos")
        for herbivoro in self.herbivoros:
            print(f"{herbivoro.nombre} (herbívoro): {herbivoro.poblacion} individuos")
        for carnivoro in self.carnivoros:
            print(f"{carnivoro.nombre} (carnívoro): {carnivoro.poblacion} individuos")

    def guardar_ecosistema(self, filename='ecosistema.json'):
        data = {
            'plantas': [{ 'nombre': p.nombre, 'poblacion': p.poblacion } for p in self.plantas],
            'herbívoros': [{ 'nombre': h.nombre, 'poblacion': h.poblacion } for h in self.herbivoros],
            'carnívoros': [{ 'nombre': c.nombre, 'poblacion': c.poblacion } for c in self.carnivoros]
        }

        with open(filename, 'w') as f:
            json.dump(data, f)
