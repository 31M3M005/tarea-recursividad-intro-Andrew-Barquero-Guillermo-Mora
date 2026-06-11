"""
Ejercicio 4
Dificultad: Fácil
Desarrolle una función recursiva llamada invertir_numero(numero) que reciba un número entero positivo y
retorne el número invertido.
No puede convertir el número a string ni a lista.
Casos de prueba:
• invertir_numero(1234) debe retornar 4321
• invertir_numero(900) debe retornar 9
• invertir_numero(5071) debe retornar 1705
• invertir_numero(8) debe retornar 8
"""
def invertir_numero(numero):#se crea la funcion principal, que ejecuta todo el proceso
    def auxiliar(n, acumulador): #Se crea una función auxiliar que hace el proceso del problema
        if n == 0: #condicion de parada
            return acumulador
        return auxiliar(n//10, acumulador * 10 + n % 10) #Llamada recursiva, que reduce el numero en 10 y suma el resultado en acumulador
    return auxiliar(abs(numero),0) #Llamada que retorna a la función auxiliardandole el int para entrar en la recursividad

print(invertir_numero(1234))
print(invertir_numero(900))
print(invertir_numero(5071))
print(invertir_numero(8))