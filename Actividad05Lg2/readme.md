
## MAIN Principal (Descripcion)

1. Importaciones:
 * Se importan las clases necesarias desde sus respectivos módulos: Ecosistema, Planta, Herbivoro, Carnivoro, y Especie. Esto permite utilizar estas clases en la función principal.

2. Función main():
 * Esta es la función principal que gestiona la simulación del ecosistema. Se encarga de interactuar con el usuario mediante un menú.

3. Creación del Ecosistema:
 * Se crea una instancia de Ecosistema, que es la clase que probablemente gestiona la lógica del ecosistema y las interacciones entre las especies.

4. Bucle Principal:
 * Un bucle while True se utiliza para mostrar un menú de opciones al usuario hasta que decida salir.

5. Menú de Opciones:
 * Se presentan seis opciones al usuario:
   1. Agregar Especie: Permite al usuario agregar una nueva especie al ecosistema. Dependiendo del tipo de especie (planta, herbívoro o carnívoro), se le piden diferentes parámetros.
   2. Simular Día: Permite al usuario simular un número específico de días en el ecosistema, invocando el método simular_dia() del ecosistema.
   3. Mostrar Estadísticas: Muestra estadísticas sobre el estado actual del ecosistema, utilizando el método mostrar_estadisticas().
   4. Guardar Ecosistema: Permite guardar el estado actual del ecosistema en un archivo, utilizando el método guardar_ecosistema().
   5. Salir: Termina el bucle y cierra el programa.

6. Agregar Especie:
 * Si el usuario selecciona la opción de agregar una especie, se le pide que ingrese el nombre, tipo y capacidad de reproducción.
 * Dependiendo del tipo de especie, se solicitan parámetros adicionales (como capacidad de búsqueda para herbívoros y carnívoros).
 * Se crea una instancia de la especie correspondiente y se agrega al ecosistema mediante el método agregar_especie().