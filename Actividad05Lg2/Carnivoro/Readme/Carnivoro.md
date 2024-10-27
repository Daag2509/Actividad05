
## Carnivoro (Descripcion)

1. Herencia:

* La clase Carnivoro hereda de la clase Especie, lo que significa que incorpora las propiedades y métodos de Especie. Esto permite que Carnivoro sea considerado un tipo de Especie, con características adicionales específicas para los carnívoros.

2. Constructor (__init__):

* El constructor de la clase Carnivoro recibe cuatro parámetros:
nombre: El nombre del carnívoro.
 * capacidad_reproduccion: La capacidad de reproducción del carnívoro, que se pasa al constructor de la clase base Especie.
 * capacidad_busqueda: Una medida de cuán eficaz es el carnívoro para buscar alimento.
 * tasa_efectividad: Un factor que determina la efectividad del carnívoro en su búsqueda de alimento.
Dentro del constructor, se inicializan los atributos específicos de la clase Carnivoro, como alimento_consumido, que comienza en 0.

3. Método buscar_alimento:

* Este método permite que el carnívoro busque alimento entre una lista de herbívoros.
Toma como argumento herbivoros, que se espera sea una lista de instancias de una clase Herbivoro.
 * El método itera a través de cada herbívoro en la lista:
Si la población del herbívoro es mayor que 0, calcula la cantidad de alimento que el carnívoro puede consumir. Esta cantidad es el mínimo entre la población del herbívoro y una fracción de la población del herbívoro, determinada por la capacidad de búsqueda y la tasa de efectividad del carnívoro.
Se reduce la población del herbívoro en la cantidad que el carnívoro ha consumido y se incrementa el total de alimento consumido por el carnívoro.
El método termina después de que el carnívoro consume alimento de un herbívoro.

4. Método morir_por_inanicion:

* Este método se encarga de manejar la muerte del carnívoro por inanición.
Verifica si el carnívoro no ha consumido alimento (es decir, alimento_consumido es igual a 0).
Si no ha consumido alimento, reduce la población del carnívoro en un 10% (0.1). Este método no tiene un retorno explícito, pero modifica el estado del objeto Carnivoro.

(Métodos Utilizados)
* super().__init__(): Se utiliza para llamar al constructor de la clase base Especie y pasarle el nombre y capacidad_reproduccion.
* min(): Se utiliza para calcular la cantidad de alimento que el carnívoro puede consumir, asegurando que no exceda la población del herbívoro.
* for: Se utiliza para iterar a través de la lista de herbívoros en el método buscar_alimento.
* if: Se utiliza para verificar condiciones, como la población del herbívoro y si el carnívoro ha consumido alimento.