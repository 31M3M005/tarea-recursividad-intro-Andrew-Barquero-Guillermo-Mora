"""
Ejercicio 2
Dificultad: Fácil
Desarrolle una función recursiva llamada contar_pares(numero) que reciba un número entero positivo y retorne
cuántos dígitos pares contiene el número.
El cero debe considerarse como dígito par.
No puede convertir el número a string ni a lista.
Casos de prueba:
• contar_pares(2486) debe retornar 4
• contar_pares(13579) debe retornar 0
• contar_pares(12040) debe retornar 4
• contar_pares(7) debe retornar 0
"""
def contar_pares(numero): #Se crea la funcion principal
    if numero == 0: #Condicion de parada
        return 0
    if (numero%10) % 2 == 0: #Si el digito menos significativo es par
        return 1 + contar_pares(numero // 10) #se suma uno y se sigue con la función del número reducido en 10
    else:
        return 0 + contar_pares(numero // 10) #Si no es par, se suma 0 y se sigue con la recursividad.

print(contar_pares(2486))
print(contar_pares(13579))
print(contar_pares(12040))
print(contar_pares(7))