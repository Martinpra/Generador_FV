import numpy as np


# Ejercicio 4
# Cargar, en un script de Python, la siguiente lista de valores numéricos:
# valores_num = [24.8, 25.6, 28.9, 27.5, 26.2, 24.5, 24.2, 23.8, 25.1, 37.2, 25.9, 26.1, 38.7, 10.1, 25.5, 24.8]
# Interpretar dichos valores como mediciones de la temperatura de un ambiente en grados centígrados, registradas en un rango horario acotado, 
# para el cual no se esperan grandes variaciones.
# Generar una segunda lista con los valores considerados de mediciones correctas, teniendo en cuenta que se consideran mediciones fallidas 
# aquellas que se apartan más allá de un 40% de la temperatura promedio (40% por encima o por debajo de la misma).

dtypes = [('hora', int), ('temperatura', float)]
valores_num = np.array([(1, 24.8), (2, 25.6), (3, 28.9), (4, 27.5), (5, 26.2),
                        (6, 24.5), (7, 24.2), (8, 23.8), (9, 25.1), (10, 37.2),
                        (11, 25.9), (12, 26.1), (13, 38.7), (14, 10.1), (15, 25.5),
                        (16, 24.8)], dtype=dtypes)

temperatura_promedio = np.mean(valores_num['temperatura'])

umbral_variacion = 0.4 * temperatura_promedio

mediciones_correctas = valores_num[(valores_num['temperatura'] >= temperatura_promedio - umbral_variacion) & 
                                   (valores_num['temperatura'] <= temperatura_promedio + umbral_variacion)]

print("Lista original de mediciones:")
print(valores_num)

print("\nLista de mediciones consideradas correctas:")
print(mediciones_correctas)




