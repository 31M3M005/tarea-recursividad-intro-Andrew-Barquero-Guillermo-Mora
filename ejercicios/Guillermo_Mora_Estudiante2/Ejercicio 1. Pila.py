"""
Ejercicio 1
Dificultad: Fácil
Desarrolle una función recursiva llamada sumar_digitos(numero) que reciba un número entero positivo y retorne
la suma de todos sus dígitos.
No puede convertir el número a string ni a lista.
Casos de prueba:
• sumar_digitos(1234) debe retornar 10
• sumar_digitos(9001) debe retornar 10
• sumar_digitos(7) debe retornar 7
• sumar_digitos(0) debe retornar 0
"""
def sumar_digitos(numero): #se crea la funcion
    if numero <= 0: #se da la condición de parada
        return 0
    return (numero % 10) + sumar_digitos(numero//10) #se hace la llamada recursiva, al ultimo digito sumandole la funcion del numero reducido en 10

print(sumar_digitos(1234))
print(sumar_digitos(9001))
print(sumar_digitos(7))
print(sumar_digitos(0))