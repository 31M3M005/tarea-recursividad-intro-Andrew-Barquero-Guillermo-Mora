"""
Ejercicio 10
Dificultad: Alta
Desarrolle una función recursiva llamada comprimir_repetidos(lista) que reciba una lista de números enteros y
retorne una lista de listas, donde cada sublista contenga el número y la cantidad de veces consecutivas que
aparece.
Casos de prueba:
• comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]) debe retornar [[1, 3], [2, 2], [3, 1], [1, 2]]
• comprimir_repetidos([5, 5, 5, 5]) debe retornar [[5, 4]]
• comprimir_repetidos([1, 2, 3, 4]) debe retornar [[1, 1], [2, 1], [3, 1], [4, 1]]
• comprimir_repetidos([]) debe retornar []
"""
def comprimir_repetidos(lista):
    # Caso base
    if not lista:
        return []

    # Caso base: un solo elemento
    if len(lista) == 1:
        return [[lista[0], 1]]

    # Procesar el resto de la lista
    resto = comprimir_repetidos(lista[1:])

    # Si el primer elemento es igual al siguiente bloque
    if lista[0] == resto[0][0]: #si el primer elemento de la lista es igual al primer elemento de la primer sublista del resto
        resto[0][1] += 1 #se le suma uno al contador de la primera sublista del resto
        return resto #retorna resto
    else:
        return [[lista[0], 1]] + resto #si no son iguales, se cierra la sublista y se continua con el resto de la lista

print(comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1]))
# [[1, 3], [2, 2], [3, 1], [1, 2]]

print(comprimir_repetidos([5, 5, 5, 5]))
# [[5, 4]]

print(comprimir_repetidos([1, 2, 3, 4]))
# [[1, 1], [2, 1], [3, 1], [4, 1]]

print(comprimir_repetidos([]))
# []