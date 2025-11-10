# Sistema de Gestión y Análisis de Datos de Países

## 📋 Descripción del Proyecto

Sistema completo de gestión de información sobre países desarrollado en Python utilizando únicamente las librerías estándar `csv` y `os`. Permite administrar, consultar y analizar datos geográficos y demográficos de países mediante una interfaz interactiva de menú.

**Características principales:**

- Carga automática de datos desde archivo CSV
- Gestión de datos (agregar, actualizar, eliminar)
- Búsquedas avanzadas y filtros múltiples
- Ordenamiento flexible por diferentes criterios
- Estadísticas y análisis de datos
- Persistencia automática de cambios
- Interfaz profesional con formato de tabla

---

## 🎓 Datos Académicos

**Institución:** Universidad Tecnológica Nacional (UTN)  
**Carrera:** Tecnicatura Universitaria en Programación  
**Asignatura:** Programación 1  
**Año:** 2025  
**Tipo:** Trabajo Práctico Integrador

### 👥 Integrantes

- **Agüero Maximiliano**
- **Dario Frison**

### 👨‍🏫 Profesores

- **Profesor Coordinador:**
  - Alberto Cortez
- **Profesor a cargo comisión:**
  - Cinthia Rigoni
  - Sebastián Bruselario
  - Ariel Enferrel

---

## 📁 Estructura del Proyecto

```
TPI/
│
├── Aguero_Frison.py          # Programa principal
├── paises.csv                 # Dataset de países (25 países iniciales)
└── README.md                  # Esta documentación
```

### Estructura de Datos

Cada país contiene:

- **Nombre** (string)
- **Población** (int): habitantes
- **Superficie** (int): km²
- **Continente** (string)

---

## 🚀 Instrucciones de Ejecución

### Requisitos

- Python 3.10 o superior
- No requiere instalación de librerías adicionales

### Ejecutar el programa

**IMPORTANTE:** Ejecutar desde el directorio TPI del proyecto.

```bash
cd TPI
python Aguero_Frison.py
```

Al iniciar, el programa carga automáticamente los datos desde `paises.csv`.

---

## 📚 Librerías Utilizadas

**Librerías estándar de Python (no requieren instalación):**

- `csv`: Lectura y escritura de archivos CSV
- `os`: Validación de archivos y limpieza de pantalla

**No se utilizan librerías de terceros**

---

## 🎯 Funcionalidades del Menú

### Gestión de Datos

- **[1]** Agregar país manualmente
- **[2]** Actualizar datos de país

### Consultas y Búsquedas

- **[3]** Buscar país por nombre (coincidencia parcial/exacta)
- **[4]** Filtrar por continente
- **[5]** Filtrar por rango de población
- **[6]** Filtrar por rango de superficie

### Ordenamiento

- **[7]** Ordenar por nombre (A-Z)
- **[8]** Ordenar por población
- **[9]** Ordenar por superficie

### Análisis

- **[10]** Mostrar estadísticas generales
- **[11]** Mostrar todos los países

### Salida

- **[0]** Salir del programa

---

## 💡 Ejemplos de Entrada y Salida

### Ejemplo 1: Inicio del Programa

```
>> Cargando datos iniciales desde archivo CSV...

============================================================
           RESULTADO DE CARGA DE ARCHIVO
============================================================
Paises cargados exitosamente: 25
============================================================
```

### Ejemplo 2: Agregar País

**Entrada:**

```
>> Seleccione una opcion: 1
Ingrese el nombre del país: Uruguay
Ingrese la población: 3500000
Ingrese la superficie (km²): 176215
Ingrese el continente: América Del Sur
```

**Salida:**

```
==================================================
>>> Pais 'Uruguay' agregado exitosamente! <<<
==================================================
```

### Ejemplo 3: Buscar País

**Entrada:**

```
>> Seleccione una opcion: 3
Ingrese el nombre del pais a buscar: arg
```

**Salida:**

```
Se encontraron 1 resultado(s) para 'arg':

✓ Coincidencias parciales (1):

==================================================================================
PAÍS            │ POBLACIÓN       │ SUPERFICIE      │ CONTINENTE      │ DENSIDAD
                │ (habitantes)    │ (km²)           │                 │ (hab/km²)
----------------------------------------------------------------------------------
Argentina       │  45,000,000     │   2,780,400     │ América Del Sur │      16.2
==================================================================================
```

### Ejemplo 4: Estadísticas Generales

**Entrada:**

```
>> Seleccione una opcion: 10
```

**Salida:**

```
======================================================================
                    ESTADÍSTICAS GENERALES
======================================================================

 ESTADÍSTICAS DE POBLACIÓN:
--------------------------------------------------
País con mayor población: Brasil (213,000,000 habitantes)
País con menor población: Uruguay (3,500,000 habitantes)
Población promedio: 75,100,000 habitantes

 ESTADÍSTICAS DE SUPERFICIE:
--------------------------------------------------
País con mayor superficie: Brasil (8,515,767 km²)
País con menor superficie: Uruguay (176,215 km²)
Superficie promedio: 2,524,435 km²

DISTRIBUCIÓN POR CONTINENTES:
--------------------------------------------------
América Del Sur: 2 países (40.0%)
Europa: 2 países (40.0%)
Asia: 1 países (20.0%)
======================================================================
```

---

## 🔧 Características Técnicas

### Conceptos de Programación Aplicados

- Estructuras condicionales (`if`, `elif`, `else`, `match-case`)
- Estructuras repetitivas (`for`, `while`)
- Funciones con parámetros y retorno
- Listas y diccionarios
- Manipulación de archivos CSV
- Validación preventiva de datos (sin `try/except`)
- Arquitectura modular sin variables globales

### Algoritmo de Ordenamiento

**Bubble Sort** (Ordenamiento Burbuja)

- Facil de implementar y entender
- Adecuado para conjuntos de datos pequeños

### Formato del Archivo CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45000000,2780400,América del Sur
Brasil,213000000,8515767,América del Sur
España,47000000,505990,Europa
```

**Validaciones implementadas:**

- Existencia de archivos
- Permisos de lectura
- Campos no vacíos
- Valores numéricos positivos
- Formato correcto de datos

---

## 🔗 Enlaces

- **Repositorio GitHub:**
- **Video demostración:**

---

**Desarrollado por Agüero Maximiliano y Dario Frison - UTN 2025**
