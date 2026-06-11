"""
Ejercicio 7
Dificultad: Media
Desarrolle una función recursiva llamada separar_por_paridad(numero) que reciba un número entero positivo y
retorne una lista con dos números:
El primer número debe estar formado por los dígitos pares del número original.
El segundo número debe estar formado por los dígitos impares del número original.
Se debe respetar el orden original de aparición de los dígitos.
No puede convertir el número a string ni a lista.
Casos de prueba:
• separar_por_paridad(123456) debe retornar [246, 135]
• separar_por_paridad(80231) debe retornar [802, 31]
• separar_por_paridad(97531) debe retornar [0, 97531]
• separar_por_paridad(2468) debe retornar [2468, 0]
"""
def separar_por_paridad(numero): #se crea la funcion principal
    def auxiliar(n, pares, impares, pot_pares, pot_impares): #se crea la funcion auxiliar
        if n == 0: #condicion de parada
            return [pares, impares] #retorna [0,0]

        digito = n % 10 #declara la variable a trabajar, el ultimo digito

        if digito % 2 == 0: #si el digito es par, se almacena en pares, donde se hace la suma del numero con su respectiva potencia
            pares = digito * pot_pares + pares
            pot_pares *= 10 #se aumenta la potencia en 10 por cada llamada recursiva
        else:
            impares = digito * pot_impares + impares  #si el digito es impar, se almacena en impares, donde se hace la suma del numero con su respectiva potencia
            pot_impares *= 10 #se aumenta la potencia en 10 por cada llamada recursiva

        return auxiliar(n // 10, pares, impares, pot_pares, pot_impares) #llamda recursiva de la funcion auxiliar, donde se reduce el numero en 10

    return auxiliar(numero, 0, 0, 1, 1) #se llama la funcion auxiliar para ejecutar el proceso con los datos del usuario

print(separar_por_paridad(123456))
print(separar_por_paridad(80231))
print(separar_por_paridad(97531))
print(separar_por_paridad(8))
