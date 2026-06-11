"""
Ejercicio 8
Dificultad: Media
Desarrolle una función recursiva llamada detectar_valles(lista) que reciba una lista de números enteros y retorne
una lista de listas con las secuencias de tres elementos consecutivos donde el elemento central sea menor que el
anterior y menor que el siguiente.
A estas secuencias se les llamará valles locales.
Casos de prueba:
• detectar_valles([5, 1, 6, 3, 8, 2, 7]) debe retornar [[5, 1, 6], [6, 3, 8], [8, 2, 7]]
• detectar_valles([1, 2, 3, 4, 5]) debe retornar []
• detectar_valles([9, 4, 8, 2, 6]) debe retornar [[9, 4, 8], [8, 2, 6]]
• detectar_valles([3, 1]) debe retornar []
"""
def detectar_valles(lista): #Se define la función principal
    def recursiva(i): #función auxiliar que realiza todo el proceso
        # Caso base: no quedan 3 elementos para evaluar
        if i + 2 >= len(lista):
            return [] #retorna lista vacía

        # Evaluar el trío actual
        actual = [] #se declara la variable actual como una lista vacía porque después se cambia su valor
        if lista[i+1] < lista[i] and lista[i+1] < lista[i+2]:
        #Se preparan las condiciones: secuencias de tres elementos consecutivos donde el elemento central sea menor que el anterior y menor que el siguiente.
            actual = [[lista[i], lista[i+1], lista[i+2]]] #Se le asigna el valor correcto a actual para tener la lista con los elementos

        # La pila se encarga de unir resultados
        return actual + recursiva(i + 1) #Se almacenan por medio de pilas las listas que se van creando
    return recursiva(0) #Se llama a la función auxiliar para poder arrancar el proceso con un indice 0 que va aumentando según se llame a la función recursiva.

print(detectar_valles([5, 1, 6, 3, 8, 2, 7]))
# [[5, 1, 6], [6, 3, 8], [8, 2, 7]]

print(detectar_valles([1, 2, 3, 4, 5]))
# []

print(detectar_valles([9, 4, 8, 2, 6]))
# [[9, 4, 8], [8, 2, 6]]

print(detectar_valles([3, 1]))
# []