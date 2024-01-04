import numpy as np

# Paso 1: Cargar un diccionario con nombres de alumnos y calificaciones
alumnos_calificaciones = {
    'Federico': 5.5,
    'Adriana': 9.2,
    'Exequiel': 6.8,
    'Mariana': 7.5,
    'Laura': 4.5,
    'Nanci': 2.1,
    'Raúl': 4.2,
}

print("Diccionario original:")
print(alumnos_calificaciones)

# Convertir los valores del diccionario en un array NumPy
calificaciones_array = np.array(list(alumnos_calificaciones.values()))

# Paso 2: Procesar el array NumPy para obtener aprobados y reprobados
aprobados_indices = calificaciones_array >= 6
reprobados_indices = calificaciones_array < 6

# Crear diccionarios de aprobados y reprobados
aprobados = {nombre: calificacion for nombre, calificacion in sorted(alumnos_calificaciones.items()) if calificacion >= 6}
reprobados = {nombre: calificacion for nombre, calificacion in sorted(alumnos_calificaciones.items()) if calificacion < 6}

# Imprimir listas de aprobados y reprobados
print("\nAlumnos aprobados:")
for nombre, calificacion in sorted(aprobados.items()):
    print(f"{nombre}: {calificacion}")

print("\nAlumnos reprobados:")
for nombre, calificacion in sorted(reprobados.items()):
    print(f"{nombre}: {calificacion}")
