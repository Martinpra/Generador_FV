import numpy as np

# Paso 1: Cargar un diccionario con nombres de alumnos y calificaciones
alumnos_calificaciones = {
    'Juan': 7.5,
    'María': 5.8,
    'Carlos': 9.2,
    'Laura': 4.5,
    'Pedro': 6.7,
    'Ana': 8.0,
    'José': 3.9,
    'Elena': 7.8,
    'Miguel': 5.0,
    'Sofía': 8.5
}

print("Diccionario original:")
print(alumnos_calificaciones)

# Convertir los valores del diccionario en un array NumPy
calificaciones_array = np.array(list(alumnos_calificaciones.values()))

# Paso 2: Procesar el array NumPy para obtener aprobados y reprobados
aprobados_indices = calificaciones_array >= 6
reprobados_indices = calificaciones_array < 6

# Crear diccionarios de aprobados y reprobados
aprobados = {nombre: calificacion for nombre, calificacion in alumnos_calificaciones.items() if calificacion >= 6}
reprobados = {nombre: calificacion for nombre, calificacion in alumnos_calificaciones.items() if calificacion < 6}

print("\nDiccionario de aprobados:")
print(aprobados)

print("\nDiccionario de reprobados:")
print(reprobados)
