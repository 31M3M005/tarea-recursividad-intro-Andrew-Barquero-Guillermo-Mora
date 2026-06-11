"""
Ejercicio 6
Dificultad: Media
Desarrolle una función recursiva llamada contar_bloques_iguales(lista) que reciba una lista de números enteros
y retorne la cantidad de bloques de números consecutivos iguales.
Un bloque es una secuencia continua donde el mismo número aparece una o más veces seguidas.
Casos de prueba:
• contar_bloques_iguales([1, 1, 2, 2, 2, 3, 1, 1]) debe retornar 4
• Explicación: [1,1], [2,2,2], [3], [1,1]
• contar_bloques_iguales([5, 5, 5, 5]) debe retornar 1
• contar_bloques_iguales([1, 2, 3, 4]) debe retornar 4
• contar_bloques_iguales([]) debe retornar 0
"""
def contar_bloques_iguales(lista): #se crea la funcion principal
    def auxiliar(sublista, anterior, contador): #se crea la funcion secundaria
        if not sublista: #caso de parada
            return contador

        actual = sublista[0] #se declara una abreviación para el primer elemento de la lista

        if anterior is None or actual != anterior: #condiciones: secuencia continua donde el mismo número aparece una o más veces seguidas.
            contador += 1

        return auxiliar(sublista[1:], actual, contador) #llamada recursiva de la funcion auxiliar

    return auxiliar(lista, None, 0) #se llama a la funcion auxiliar con los datos del usuario.

print(contar_bloques_iguales([5, 5, 5, 5]))
print(contar_bloques_iguales([1, 2, 3, 4]))
print(contar_bloques_iguales([]))