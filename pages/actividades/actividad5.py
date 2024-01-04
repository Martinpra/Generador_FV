import numpy as np

# Ejercicio 5
# Considerar la lista del Ejercicio 4 y, a partir de ésta, generar otra lista corregida que reemplace los valores fallidos por una estimación,
# calculada como el promedio entre el valor anterior y el posterior. A los fines de este ejercicio, obviar la posibilidad de que los valores fallidos}
# se ubiquen en el primer y último lugar.
valores_num = np.array([24.8, 25.6, 28.9, 27.5, 26.2, 24.5, 24.2, 23.8, 25.1, 37.2, 25.9, 26.1, 38.7, 10.1, 25.5, 24.8])

temperatura_promedio = np.mean(valores_num)

umbral_variacion = 0.4 * temperatura_promedio

indices_fallidos = np.where(np.abs(valores_num - temperatura_promedio) > umbral_variacion)[0]

valores_corregidos = np.copy(valores_num)

for indice in indices_fallidos:
    if 0 < indice < len(valores_num) - 1:
        valores_corregidos[indice] = (valores_num[indice - 1] + valores_num[indice + 1]) / 2.0


print("Lista original de mediciones:")
print(valores_num)

print("\nLista corregida:")
print(valores_corregidos)
