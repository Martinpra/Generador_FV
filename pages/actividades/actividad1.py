import numpy as np

# Paso 1: Cargar una lista o tupla con números enteros o decimales en el rango de 0 a 10
num_calificaciones = 10
calificaciones = []

print("Por favor, ingrese las calificaciones de los alumnos:")

for i in range(num_calificaciones):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
                break
            else:
                print("La calificación debe estar en el rango de 0 a 10. Inténtelo de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")

calificaciones = np.array(calificaciones)

print("\nCalificaciones originales:")
print(calificaciones)

# Paso 2: Filtrar las calificaciones mayores o iguales a 6 (aprobados)
aprobados = calificaciones[calificaciones >= 6]

print("\nCalificaciones de los aprobados:")
print(aprobados)
