
## Ecosistema (Descripcion)

1. Atributos:

 * plantas: Lista que almacena las instancias de la clase Planta.
 * herbivoros: Lista que almacena las instancias de la clase Herbivoro.
 * carnivoros: Lista que almacena las instancias de la clase Carnivoro.

2. Métodos:

* __init__:
Constructor que inicializa las listas vacías para plantas, herbívoros y carnívoros.
* agregar_especie(self, especie):
 Este método permite agregar una especie al ecosistema.
Recibe un objeto especie y verifica su tipo utilizando isinstance().
Dependiendo del tipo, agrega la especie a la lista correspondiente (plantas, herbivoros o carnivoros).
* simular_dia(self):
 Simula un día en el ecosistema, ejecutando las interacciones y ciclos de vida de las especies.
 * Crecimiento de plantas: Llama al método crecer() en cada planta para simular su crecimiento.
Búsqueda de alimento por herbívoros: Los herbívoros buscan alimento en las plantas, ordenados por su capacidad de búsqueda.
Búsqueda de alimento por carnívoros: Los carnívoros buscan alimento en los herbívoros, ordenados por su capacidad de búsqueda multiplicada por su tasa de efectividad.
Mortalidad por inanición: Se verifica si los herbívoros y carnívoros han consumido alimento y se llama al método morir_por_inanicion() en caso de que no lo hayan hecho.
Reproducción: Se llama al método reproducirse() en plantas, así como en herbívoros y carnívoros que han consumido alimento.
 * mostrar_estadisticas(self):
Imprime las estadísticas del ecosistema, mostrando el nombre y la población de cada tipo de especie (plantas, herbívoros y carnívoros).
 * guardar_ecosistema(self, filename='ecosistema.json'):
Guarda el estado actual del ecosistema en un archivo JSON.
Crea un diccionario que contiene la información de las plantas, herbívoros y carnívoros, y la escribe en el archivo especificado.
 * cargar_ecosistema(self, filename='ecosistema.json'):
Carga el estado del ecosistema desde un archivo JSON.
Intenta abrir el archivo y cargar los datos. Si el archivo no existe, se captura la excepción FileNotFoundError.
Recorre los elementos del archivo JSON, crea instancias de las especies correspondientes y las agrega al ecosistema usando el método agregar_especie().
Imprime un mensaje de éxito si se carga correctamente o un mensaje de error si el archivo no se encuentra.

(Métodos Utilizados)

 * `isinstance(): Se utiliza para verificar si un objeto es de un tipo específico (por ejemplo, si es una Planta, Herbivoro o Carnivoro).
 * sorted(): Se utiliza para ordenar las listas de herbívoros y carnívoros según su capacidad de búsqueda o capacidad de búsqueda multiplicada por la tasa de efectividad, respectivamente.
 * print(): Se utiliza para mostrar información en la consola, como estadísticas del ecosistema y mensajes de éxito o error.