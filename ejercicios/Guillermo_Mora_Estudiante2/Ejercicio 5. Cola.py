"""
Ejercicio 5
Dificultad: Fácil
Desarrolle una función recursiva llamada eliminar_impares(numero) que reciba un número entero positivo y
retorne un nuevo número formado únicamente por los dígitos pares del número original.
Si el número no contiene dígitos pares, debe retornar 0.
No puede convertir el número a string ni a lista.
Casos de prueba:
• eliminar_impares(123456) debe retornar 246
• eliminar_impares(97531) debe retornar 0
• eliminar_impares(80246) debe retornar 80246
• eliminar_impares(1007) debe retornar 0
"""
def eliminar_impares(numero): #se crea la funcion principal que llama a la funcion secundaria
    def auxiliar(numero, acumulador, pot): #se crea la funcion auxiliar que hace todo el proceso para solucionar el problema
        if numero == 0: #condicion de parada o caso base
            return acumulador
        ultimo = numero % 10 #se declara la variable del ultimo digito para abreviar
        resto = numero // 10 #se declara la variable que reduce el número para abreviar
        if ultimo % 2 == 0: #se comprueba si es par
            acumulador = ultimo * pot + acumulador #Se suma en el acumulador cuando es par
            pot *= 10 #se aumenta la potencia con cada llamada para coincidir con el valor correcto del digito
        return auxiliar(resto, acumulador,pot) #Se hace la llamada recursiva
    return auxiliar(numero, 0, 1) #se ejecuta la función secundaria con el valor brindado por el usuario

print(eliminar_impares(123456))
print(eliminar_impares(97531))
print(eliminar_impares(80246))
print(eliminar_impares(1007))