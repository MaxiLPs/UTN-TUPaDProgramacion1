# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("--------------- Ejercicio 1 --------------- ")
for numero in range(101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("--------------- Ejercicio 2 --------------- ")
numero = int(input("Ingrese un número entero: "))
digitos = 0
while numero > 0:
    numero //= 10
    digitos += 1
print("La cantidad de dígitos es:", digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("--------------- Ejercicio 3 --------------- ")
valor1 = int(input("Ingrese el primer valor (entero): "))
valor2 = int(input("Ingrese el segundo valor (entero): "))
suma = 0
for numero in range(valor1 + 1, valor2):
    suma += numero
print("La suma de los números entre", valor1, "y", valor2, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("--------------- Ejercicio 4 --------------- ")
total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    total += numero
print("El total acumulado es:", total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("--------------- Ejercicio 5 --------------- ")
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        break
print("Adivinaste el número en", intentos, "intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("--------------- Ejercicio 6 --------------- ")
for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("--------------- Ejercicio 7 --------------- ")
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for numero in range(limite + 1):
    suma += numero
print("La suma de los números entre 0 y", limite, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("--------------- Ejercicio 8 --------------- ")
pares = 0
impares = 0
negativos = 0
positivos = 0
cantidad = 10  # Cambiar este valor para probar con menos números
for i in range(cantidad):
    numero = int(input(f"Ingrese un número entero ({i + 1}/{cantidad}): "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
print("Números pares:", pares)
print("Números impares:", impares)
print("Números negativos:", negativos)
print("Números positivos:", positivos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("--------------- Ejercicio 9 --------------- ")
suma = 0
cantidad2 = 10  # Cambiar este valor para probar con menos números
for i in range(cantidad2):
    numero = int(input(f"Ingrese un número entero ({i + 1}/{cantidad2}): "))
    suma += numero
media = suma / cantidad2
print("La media de los números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("--------------- Ejercicio 10 --------------- ")
numero = int(input("Ingrese un número entero: "))
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10
print("El número invertido es:", invertido)