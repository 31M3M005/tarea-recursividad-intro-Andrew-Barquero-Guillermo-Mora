"""
Ejercicio 9
Dificultad: Alta
Desarrolle una función recursiva llamada sublistas_ascendentes(lista) que reciba una lista de números enteros y
retorne una lista de sublistas.
Cada sublista debe contener una secuencia de números consecutivos estrictamente ascendentes.
Cuando el siguiente número sea menor o igual que el anterior, se debe iniciar una nueva sublista.
No puede usar ciclos.
Casos de prueba:
• sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]) debe retornar [[1, 2, 3], [1, 4, 5], [2]]
• sublistas_ascendentes([5, 4, 3, 2]) debe retornar [[5], [4], [3], [2]]
• sublistas_ascendentes([1, 3, 5, 7]) debe retornar [[1, 3, 5, 7]]
• sublistas_ascendentes([2, 2, 3, 1, 2]) debe retornar [[2], [2, 3], [1, 2]]
• sublistas_ascendentes([]) debe retornar []
"""
def sublistas_ascendentes(lista): #se crea la funcion principal

    def aux(i, actual, resultado): #se crea la funcion secundaria
        # Caso base: se terminó la lista
        if i == len(lista):
            if actual:
                resultado.append(actual)
            return resultado

        # Si es el primer elemento o sigue siendo ascendente
        if not actual or lista[i] > actual[-1]: #determina si el elemento que se está comparando es mayor que el anterior o no
            actual.append(lista[i]) # en caso de serlo, se agrega a la sublista
        else:
            resultado.append(actual) #si no lo es, se agrega la sublista al resultado, dejando vacía a la sublista actual
            actual = [lista[i]] #para agregarle el nuevo elemento a la nueva sublista

        return aux(i + 1, actual, resultado) #llamada recursiva

    return aux(0, [], []) #llamada a la funcion auxiliar con los datos del usuario.
print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))
print(sublistas_ascendentes([5, 4, 3, 2]))
print(sublistas_ascendentes([1, 3, 5, 7]))
print(sublistas_ascendentes([2, 2, 3, 1, 2]))
print(sublistas_ascendentes([]))

