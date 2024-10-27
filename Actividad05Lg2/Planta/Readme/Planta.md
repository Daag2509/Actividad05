
## Planta (Descripcion)

1. Herencia:
 * La clase Planta hereda de la clase Especie, lo que significa que incorpora las propiedades y métodos de la clase base. Esto permite que Planta sea considerada un tipo de Especie, con características y comportamientos específicos para las plantas.

2. Atributos:
 * Al igual que en la clase Especie, la clase Planta tiene los atributos nombre, capacidad_reproduccion y poblacion. Estos atributos se inicializan a través del constructor de la clase base.

3. Métodos:
 * __init__(self, nombre, capacidad_reproduccion):
Constructor que inicializa los atributos de la clase.
 * Recibe dos parámetros: nombre (el nombre de la planta) y capacidad_reproduccion (la probabilidad de que la planta se reproduzca).
Llama al constructor de la clase base Especie usando super() para inicializar el nombre y la capacidad de reproducción.
 * crecer(self):
Este método simula el crecimiento de la planta.
Llama al método reproducirse() de la clase base Especie, que gestiona la reproducción de la planta.
Dado que la reproducción también puede aumentar la población de la planta, este método permite que las plantas crezcan y se multipliquen en el ecosistema.