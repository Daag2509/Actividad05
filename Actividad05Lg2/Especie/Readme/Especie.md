
## Especie (Descripcion)

1. Atributos:
 * nombre: Almacena el nombre de la especie.
 * capacidad_reproduccion: Un valor que indica la probabilidad de que la especie se reproduzca en un ciclo dado. Este valor debe estar entre 0 y 1, donde 0 significa que no se reproduce y 1 significa que se reproduce siempre.
 * poblacion: Representa la cantidad de individuos de la especie en el ecosistema. Se inicializa en 10.

2. Métodos:

 * __init__(self, nombre, capacidad_reproduccion):
Constructor que inicializa los atributos de la clase.
Recibe dos parámetros: nombre (el nombre de la especie) y capacidad_reproduccion (la probabilidad de reproducción).
Inicializa la población en 10.
 * reproducirse(self):
Este método simula el proceso de reproducción de la especie.
Utiliza random.random() para generar un número aleatorio entre 0 y 1.
Si el número aleatorio es menor que self.capacidad_reproduccion, se considera que la especie se reproduce.
  * Si se reproduce, la población de la especie aumenta en un porcentaje de su población actual, calculado como int(self.poblacion * 
  * self.capacidad_reproduccion). Esto significa que la cantidad de nuevos individuos que se añaden es proporcional a la población existente y a la capacidad de reproducción.