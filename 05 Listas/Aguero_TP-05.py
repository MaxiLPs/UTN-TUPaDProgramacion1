# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
print("--------------- Ejercicio 1 --------------- ")
notas = []
cantidad_estudiantes = 10
for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    notas.append(nota)
print("Lista de notas:", notas)
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
print("--------------- Ejercicio 2 --------------- ")
productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(producto)
print("Lista de productos ordenada:", sorted(productos))
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Lista actualizada de productos:", productos)
else:
    print("El producto no se encuentra en la lista.")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
print("--------------- Ejercicio 3 --------------- ")
import random
numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:", numeros)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números impares:", impares)
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

# 4) Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
print("--------------- Ejercicio 4 --------------- ")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []

for dato in datos:
    if dato not in datos_sin_repetidos:
        datos_sin_repetidos.append(dato)

print("Lista sin elementos repetidos:", datos_sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
print("--------------- Ejercicio 5 --------------- ")
estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    estudiantes.append(nombre)
print("Lista de estudiantes:", estudiantes)
accion = input("¿Desea agregar (A) o eliminar (E) un estudiante? ").upper()
if accion == 'A':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Lista actualizada de estudiantes:", estudiantes)
elif accion == 'E':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Lista actualizada de estudiantes:", estudiantes)
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Acción no reconocida. No se realizaron cambios.")
  
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).
print("--------------- Ejercicio 6 --------------- ")
numeros = []
for i in range(7):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
print("Lista original:", numeros)
# Rotar a la derecha
ultima = numeros.pop()  # Elimina y obtiene el último elemento
numeros.insert(0, ultima)  # Inserta el último elemento al inicio
print("Lista rotada a la derecha:", numeros)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
print("--------------- Ejercicio 7 --------------- ")
temperaturas = []
for i in range(7):
    temp_min = float(input(f"Ingrese la temperatura mínima del día {i + 1}: "))
    temp_max = float(input(f"Ingrese la temperatura máxima del día {i + 1}: "))
    temperaturas.append([temp_min, temp_max])
print("Matriz de temperaturas (mínimas y máximas):", temperaturas)

suma_min = sum(temp[0] for temp in temperaturas)
suma_max = sum(temp[1] for temp in temperaturas)
promedio_min = suma_min / 7
promedio_max = suma_max / 7

print("Promedio de temperaturas mínimas:", promedio_min)
print("Promedio de temperaturas máximas:", promedio_max)

amplitudes = [temp[1] - temp[0] for temp in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1

print("Día con mayor amplitud térmica:", dia_mayor_amplitud, "con una amplitud de", mayor_amplitud)

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
print("--------------- Ejercicio 8 --------------- ")
notas = []
for i in range(5):
    estudiante_notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota del estudiante {i + 1} en la materia {j + 1}: "))
        estudiante_notas.append(nota)
    notas.append(estudiante_notas)

# Calcular y mostrar el promedio de cada estudiante
for i, estudiante in enumerate(notas):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Promedio del estudiante {i + 1}: {promedio}")

# Calcular y mostrar el promedio de cada materia
for j in range(3):
    promedio = sum(estudiante[j] for estudiante in notas) / len(notas)
    print(f"Promedio de la materia {j + 1}: {promedio}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
print("--------------- Ejercicio 9 --------------- ")
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()
mostrar_tablero(tablero)
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    fila = int(input(f"Jugador {jugador}, ingrese la fila (0-2): "))
    columna = int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        mostrar_tablero(tablero)
    else:
        print("Casilla ya ocupada, intente de nuevo.")
        turno -= 1  # Repetir el turno
print("Juego terminado.")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.
print("--------------- Ejercicio 10 --------------- ")
ventas = []
for i in range(4):
    producto_ventas = []
    for j in range(7):
        venta = float(input(f"Ingrese las ventas del producto {i + 1} en el día {j + 1}: "))
        producto_ventas.append(venta)
    ventas.append(producto_ventas)
# Total vendido por cada producto
for i, producto in enumerate(ventas):
    total_producto = sum(producto)
    print(f"Total vendido del producto {i + 1}: {total_producto}")

# Día con mayores ventas totales
ventas_dia = [sum(ventas[i][j] for i in range(4))
                for j in range(7)]
dia_mayores_ventas = ventas_dia.index(max(ventas_dia)) + 1
print("Día con mayores ventas totales: Día", dia_mayores_ventas)

# Producto más vendido en la semana
total_productos = [sum(producto) for producto in ventas]
producto_mas_vendido = total_productos.index(max(total_productos)) + 1
print("Producto más vendido en la semana: Producto", producto_mas_vendido)

