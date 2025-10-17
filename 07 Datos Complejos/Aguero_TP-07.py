# Dominar el uso de estructuras de datos complejas en Python para
# almacenar, organizar y manipular datos de manera eficiente, aplicando
# buenas prácticas y optimizando el rendimiento de las aplicaciones

# Resultados de aprendizaje:
# 1. Comprensión y aplicación de iterables: listas, tuplas y sets.
# 2. Introducción a estructuras de datos complejas: diccionarios.


# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
print("--------------- Ejercicio 1 --------------- ")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
print("--------------- Ejercicio 2 --------------- ")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
print("--------------- Ejercicio 3 --------------- ")
frutas = list(precios_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
# contactos = {"Juan": "123456", "Ana": "987654"}
# Consultar : "Juan" -> nuestra "123456"
print("--------------- Ejercicio 4 --------------- ")
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
print(contactos.get(nombre_consulta, "Contacto no encontrado"))

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
# Entrada "hola mundo hola"
# Salida:
# Palabras_únicas: {'hola', 'mundo'}
# Recuento: {'hola': 2, 'mundo': 1}
print("--------------- Ejercicio 5 --------------- ")
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# alumnos = {
# "Sofía": (10, 9, 8),
# "Luis": (6, 7, 7)
# }
print("--------------- Ejercicio 6 --------------- ")
cantidad_notas = 3
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {_ + 1} de {nombre}: ")) for _ in range(cantidad_notas))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("--------------- Ejercicio 7 --------------- ")
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107, 108}

aprobados_ambos = set()
for estudiante in parcial_1:
    if estudiante in parcial_2:
        aprobados_ambos.add(estudiante)

aprobados_solo_uno = set()
for estudiante in parcial_1:
    if estudiante not in parcial_2:
        aprobados_solo_uno.add(estudiante)
for estudiante in parcial_2:
    if estudiante not in parcial_1:
        aprobados_solo_uno.add(estudiante)

aprobados_al_menos_uno = set()
for estudiante in parcial_1:
    aprobados_al_menos_uno.add(estudiante)
for estudiante in parcial_2:
    aprobados_al_menos_uno.add(estudiante)

print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados solo en uno de los parciales:", aprobados_solo_uno)
print("Aprobados en al menos un parcial:", aprobados_al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
print("--------------- Ejercicio 8 --------------- ")
stock_productos = {}
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'nuevo' (o 'salir' para terminar): ").lower()
    
    if accion == 'salir':
        break
    
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    match accion:
        case 'consultar':
            print(f"El stock de {nombre_producto} es: {stock_productos.get(nombre_producto, 0)}")
        case 'agregar':
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            if nombre_producto in stock_productos:
                stock_productos[nombre_producto] += cantidad
            else:
                print(f"El producto {nombre_producto} no existe en el stock.")
        case 'nuevo':
            cantidad = int(input("Ingrese la cantidad inicial del nuevo producto: "))
            stock_productos[nombre_producto] = cantidad
        case _:
            print("Acción no reconocida.")
print("Stock final de productos:", stock_productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# agenda = {
# ("lunes", "18:00"): "Reunión",
# ("martes", "15:00"): "Clase de inglés"
# }
# Permití consultar qué actividad hay en cierto día y hora.
print("--------------- Ejercicio 9 --------------- ")
agenda = {
    ("lunes", "18:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (formato HH:MM): ")

evento = agenda.get((dia, hora), "No hay actividad programada en ese día y hora.")
print(evento)
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
# original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
print("--------------- Ejercicio 10 --------------- ")
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)
