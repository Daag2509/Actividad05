
## Herbivoro (Descripcion)

1. Herencia:
 * La clase Herbivoro hereda de la clase Especie, lo que significa que incorpora las propiedades y métodos de la clase base. Esto permite que Herbivoro sea considerado un tipo de Especie, con características y comportamientos adicionales específicos para los herbívoros.

2. Atributos:
 * capacidad_busqueda: Un valor que indica la eficacia del herbívoro para buscar alimento. Este valor se utiliza para determinar cuántas plantas puede consumir.
 * velocidad_digestion: Un atributo que podría representar la rapidez con la que el herbívoro digiere el alimento consumido (aunque no se utiliza en el código proporcionado).
 * alimento_consumido: Un contador que lleva la cuenta de la cantidad de alimento que ha consumido el herbívoro, inicializado en 0.

3. Métodos:

 * __init__(self, nombre, capacidad_reproduccion, capacidad_busqueda,  velocidad_digestion):
Constructor que inicializa los atributos de la clase.
 * Recibe cuatro parámetros: nombre (el nombre del herbívoro), capacidad_reproduccion (probabilidad de reproducción), capacidad_busqueda (eficacia en la búsqueda de alimento) y velocidad_digestion (rapidez de digestión).
Llama al constructor de la clase base Especie usando super() para inicializar el nombre y la capacidad de reproducción.
 * buscar_alimento(self, plantas):
Este método permite que el herbívoro busque alimento entre una lista de plantas.
Toma como argumento plantas, que se espera que sea una lista de instancias de la clase Planta.
 * Itera a través de cada planta en la lista:
Si la población de la planta es mayor que 0, calcula la cantidad de alimento que el herbívoro puede consumir. Esta cantidad es el mínimo entre la población de la planta y una fracción de la población de la planta, determinada por la capacidad de búsqueda del herbívoro.
Se reduce la población de la planta en la cantidad que el herbívoro ha consumido y se incrementa el total de alimento consumido por el herbívoro.
El método termina después de que el herbívoro consume alimento de una planta.
 * morir_por_inanicion(self):
Este método se encarga de manejar la muerte del herbívoro por inanición.
Verifica si el herbívoro no ha consumido alimento (es decir, alimento_consumido es igual a 0).
Si no ha consumido alimento, reduce la población del herbívoro en un 10% (0.1). Este método no tiene un retorno explícito, pero modifica el estado del objeto Herbivoro.