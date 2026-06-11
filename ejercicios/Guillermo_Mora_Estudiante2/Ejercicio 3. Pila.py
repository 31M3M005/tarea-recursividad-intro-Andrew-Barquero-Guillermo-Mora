"""
Ejercicio 3
Dificultad: Fácil
Desarrolle una función recursiva llamada mayor_lista(lista) que reciba una lista de números enteros y retorne el
número mayor de la lista.
No puede utilizar la función max().
Casos de prueba:
• mayor_lista([4, 8, 1, 9, 3]) debe retornar 9
• mayor_lista([10, 2, 5, 7]) debe retornar 10
• mayor_lista([-3, -8, -1, -10]) debe retornar -1
• mayor_lista([6]) debe retornar 6
"""
def mayor_lista(lista): #se crea la funcion principal
    if len(lista) == 1: #Caso de parada
        return lista[0]

    mayor = mayor_lista(lista[1:]) #se declara una variable con la recursividad para abreviar y ver más claro el código

    if mayor < lista[0]: #Si el número declarado mayor, es menor que el siguiente elemento de la lista, se retorna el valor siguiente
        return lista[0]
    else:
        return mayor #si por el contrario, el mayor es, efectivamente mayor, se retorna la variable mayor

print(mayor_lista([4, 8, 1, 9, 3]))
print(mayor_lista([10, 2, 5, 7]))
print(mayor_lista([-3, -8, -1, -10]))
print(mayor_lista([6]))