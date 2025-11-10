# Objetivo del trabajo
# Aplicar los conceptos aprendidos sobre:
#     • Estructuras secuenciales, condicionales y repetitivas.
#     • Funciones y modularización.
#     • Listas y diccionarios.
#     • Manejo de excepciones.
#     • Persistencia de datos mediante archivos CSV.

# El propósito es crear un pequeño sistema de registro de productos que permita gestionar
# información de forma sencilla y persistente, utilizando menús y estructuras claras.

# Consigna General
# Desarrollá un programa en Python que permita administrar una lista de productos con las
# siguientes funcionalidades obligatorias:
#   1. Mostrar todos los productos registrados.
#     o Los datos deben leerse desde un archivo productos.csv.
#     o Si el archivo no existe, debe crearse automáticamente con los encabezados (nombre, precio).
#     o Mostrar cada producto con su nombre y precio, y al final el total acumulado de precios.
#   2. Agregar un nuevo producto.
#     o Pedir al usuario el nombre y el precio.
#     o Validar que el precio sea numérico y positivo.
#     o Guardar el nuevo producto en el archivo sin borrar los anteriores.
#   3. Editar (Actualizar) el precio de un producto existente.
#     o Pedir al usuario el nombre del producto a modificar.
#     o Buscar el producto por nombre. Si lo encuentra, pedir el nuevo precio, validar que sea numérico y positivo, y modificarlo en el archivo CSV.
#     o Si no existe, mostrar un mensaje de error.
#   4. Eliminar un producto existente.
#     o Pedir al usuario el nombre del producto a eliminar.
#     o Si el producto existe, eliminarlo del archivo.
#     o Si no existe, mostrar un mensaje de error.
#   5. Salir del programa.
#     o Finaliza la ejecución del menú.

# Requisitos Técnicos
# Tu programa debe cumplir con las siguientes condiciones:
#   • El menú debe repetirse hasta que el usuario elija la opción "Salir".
#   • El programa debe usar funciones para cada operación (mostrar, agregar, editar, eliminar, etc.) para modularizar el código.
#   • Los productos deben manejarse como diccionarios con claves "nombre" y "precio".
#   • El archivo debe manejarse en formato CSV usando el módulo csv de Python.
#   • No se permite el uso de manejo de excepciones (try / except).
#   • No se permite el uso de recursividad.
#   • El código debe estar correctamente identado y comentado.
import csv
import os

NOMBRE_ARCHIVO = 'productos.csv'

# Funciones auxiliares
def inicializar_archivo_productos():
    """
    Verifica si el archivo de productos existe; si no, lo crea con los encabezados adecuados.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['nombre', 'precio'])

def producto_existe(productos, nombre):
    """
    Verifica si un producto con el nombre dado ya existe en la lista de productos.
    
    Argumentos:
        productos (list): Lista de productos existentes.
        nombre (str): Nombre del producto a buscar.
    
    Retorna:
        bool: True si el producto existe, False en caso contrario.
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower().strip():
            return True
    return False

def validar_precio(precio_input):
    """
    Valida que el precio ingresado sea un número positivo.

    Argumentos:
        precio_input (str): Precio ingresado por el usuario.
    
    Retorna:
        bool: True si el precio es válido, False en caso contrario.
    """
    precio_normalizado = precio_input.strip()
    
    if precio_normalizado.count('.') > 1:
        return False
    if not precio_normalizado.replace('.', '', 1).isdigit() or float(precio_normalizado) <= 0:
        return False
    return True

def buscar_producto(productos, nombre):
    """
    Busca y retorna un producto por su nombre.
    
    Argumentos:
        productos (list): Lista de productos existentes.
        nombre (str): Nombre del producto a buscar.
    
    Retorna:
        dict or None: El producto si se encuentra, None en caso contrario.
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower().strip():
            return producto
    return None

def guardar_productos(productos):
    """
    Guarda la lista de productos en el archivo CSV.
    """
    with open(NOMBRE_ARCHIVO, mode='w', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
        writer.writeheader()
        for prod in productos:
            writer.writerow(prod)

# Funciones principales
def leer_productos():
    """
    Lee los productos desde el archivo CSV y los devuelve como una lista de diccionarios.
    """
    productos = []

    with open(NOMBRE_ARCHIVO, mode='r', newline='') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            productos.append({'nombre': fila['nombre'], 'precio': float(fila['precio'])})
    return productos

def mostrar_menu():
    """
    Muestra el menú de opciones y retorna la opción seleccionada por el usuario.
    """
    print("="*40)
    print("\nMenú de Gestión de Productos")
    print("1. Mostrar todos los productos")
    print("2. Agregar un nuevo producto")
    print("3. Editar el precio de un producto existente")
    print("4. Eliminar un producto existente")
    print("5. Salir")
    print("="*40)
    opcion = input("Seleccione una opción (1-5): ").strip()
    return opcion

def mostrar_productos(productos):
    """
    Muestra todos los productos registrados y el total acumulado de precios.
    """

    if not productos:
        print("No hay productos registrados.")
        return

    total_acumulado = 0
    print("\nProductos Registrados:")
    print("-" * 50)
    print(f"{'Nombre':<30} {'Precio':>15}")
    print("-" * 50)
    for producto in productos:
        print(f"{producto['nombre']:<30} ${producto['precio']:>14.2f}")
        total_acumulado += producto['precio']
    print("-" * 50)
    print(f"{'Total Acumulado:':<30} ${total_acumulado:>14.2f}")
    print("-" * 50)

def agregar_producto(productos):
    """
    Agrega un nuevo producto a la lista y lo guarda en el archivo CSV.

    Argumentos:
        productos (list): Lista de productos existentes.
    """
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return

    if producto_existe(productos, nombre):
        print(f"Error: El producto '{nombre}' ya existe.")
        return
    
    precio_input = input("Ingrese el precio del producto (en formato 0.00): ").strip()
    
    if not validar_precio(precio_input):
        print("Error: El precio debe ser un número positivo o válido.")
        return

    precio = float(precio_input)

    productos.append({'nombre': nombre, 'precio': precio})
    guardar_productos(productos)
    
    print(f"Producto '{nombre}' agregado exitosamente.")


def editar_producto(productos):
    """
    Edita el precio de un producto existente.
    
    Argumentos:
        productos (list): Lista de productos existentes.
    """
    if not productos:
        print("No hay productos registrados para ser modificados.")
        return
    
    nombre = input("Ingrese el nombre del producto a editar: ").strip()
    
    producto = buscar_producto(productos, nombre)
    
    if producto is None:
        print(f"Error: El producto '{nombre}' no existe.")
        return

    nuevo_precio_input = input("Ingrese el nuevo precio del producto (en formato 0.00): ").strip()

    if not validar_precio(nuevo_precio_input):
        print("Error: El precio debe ser un valor numérico positivo, en formato 0.00.")
        return

    nuevo_precio = float(nuevo_precio_input)
    producto['precio'] = nuevo_precio

    guardar_productos(productos)

    print(f"Producto '{nombre}' actualizado exitosamente.")

def eliminar_producto(productos):
    """
    Elimina un producto existente de la lista y del archivo CSV.
    
    Argumentos:
        productos (list): Lista de productos existentes.
    """
    if not productos:
        print("No hay productos registrados para ser eliminados.")
        return
    
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    if nombre == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return
    
    if not producto_existe(productos, nombre):
        print(f"Error: El producto '{nombre}' no existe.")
        return

    # Alternativa usando comprensión de listas, pero no lo utiliza en el video de ejemplo
    # productos.remove(producto) 
    
    # uso en su lugar comprensión de listas para eliminar el producto
    productos = [p for p in productos if p['nombre'].lower() != nombre.lower().strip()]

    guardar_productos(productos)

    print(f"Producto '{nombre}' eliminado exitosamente.")

# Función principal del programa

inicializar_archivo_productos()

while True:
    opcion = mostrar_menu()
    productos = leer_productos()

    match opcion:
        case '1':
            mostrar_productos(productos)
        case '2':
            agregar_producto(productos)
        case '3':
            editar_producto(productos)
        case '4':
            eliminar_producto(productos)
        case '5':
            print("Saliendo del programa. ¡Muchas gracias!")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
