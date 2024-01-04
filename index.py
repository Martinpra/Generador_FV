import pandas as pd

import matplotlib.pyplot as plt
import os
carpeta = os.path.dirname(__file__)
ruta_excel = os.path.join(carpeta, 'Datos_climatologicos_Santa_Fe_2019.xlsx')
df = pd.read_excel(ruta_excel)


def irrad_temp(d, m, h, mi):
    fecha_hora_str = f'{d:02d}-{m:02d}-2019 {h:02d}:{mi:02d}'
    try:
        fila = df.loc[df['Fecha'] == fecha_hora_str, ['Temperatura (°C)', 'Irradiancia (W/m²)']].iloc[0]
        temperatura = fila['Temperatura (°C)']
        irradiancia = fila['Irradiancia (W/m²)']

        return irradiancia, temperatura
    except IndexError:
        print(f'No se encontraron datos de temperatura para {fecha_hora_str}')


resultado = irrad_temp(20, 7, 12, 50)
print('irrad_temp:', resultado)


class DatosClimatologicos:
    def __init__(self, ruta_archivo):
        self.df = pd.read_excel(ruta_archivo)

    def buscar_irradiancia_temperatura(self, d, m, h, mi):
        fecha_hora_str = f'{d:02d}-{m:02d}-2019 {h:02d}:{mi:02d}'
        try:
            fila = self.df.loc[self.df['Fecha'] == fecha_hora_str, ['Temperatura (°C)', 'Irradiancia (W/m²)']].iloc[0]
            temperatura = fila['Temperatura (°C)']
            irradiancia = fila['Irradiancia (W/m²)']
            return irradiancia, temperatura
        except IndexError:
            print(f'No se encontraron datos de temperatura para {fecha_hora_str}')

# Ejemplo de uso
datos_climatologicos = DatosClimatologicos('Datos_climatologicos_Santa_Fe_2019.xlsx')
resultado = datos_climatologicos.buscar_irradiancia_temperatura(20, 7, 12, 50)
print('irrad_temp:', resultado)


def irrad_temp_rango(tupla1, tupla2):
    fecha_hora1_str = f'{tupla1[0]:02d}-{tupla1[1]:02d}-2019 {tupla1[2]:02d}:{tupla1[3]:02d}'
    fecha_hora2_str = f'{tupla2[0]:02d}-{tupla2[1]:02d}-2019 {tupla2[2]:02d}:{tupla2[3]:02d}'
    try:
        datos_rango = df[(df['Fecha'] >= fecha_hora1_str) & (df['Fecha'] <= fecha_hora2_str)]
        resultados = []
        for _, fila in datos_rango.iterrows():
            temperatura = fila['Temperatura (°C)']
            irradiancia = fila['Irradiancia (W/m²)']
            tupla_irrad_temp = (irradiancia, temperatura)
            resultados.append(tupla_irrad_temp)

        return resultados
    except IndexError:
        print('No se encontraron datos en el rango de fechas proporcionado')


tupla_inicio = (4, 1, 18, 20)
tupla_fin = (4, 2, 8, 40)
resultados_rango = irrad_temp_rango(tupla_inicio, tupla_fin)
print('Rango de la tabla:')
for resultado in resultados_rango:
    print(resultado)
    
    
    
class DatosClimatologicos:
    def __init__(self, ruta_archivo):
        self.df = pd.read_excel(ruta_archivo)

    def buscar_irradiancia_temperatura(self, tupla):
        fecha_hora_str = f'{tupla[0]:02d}-{tupla[1]:02d}-2019 {tupla[2]:02d}:{tupla[3]:02d}'
        try:
            fila = self.df.loc[self.df['Fecha'] == fecha_hora_str, ['Temperatura (°C)', 'Irradiancia (W/m²)']].iloc[0]
            temperatura = fila['Temperatura (°C)']
            irradiancia = fila['Irradiancia (W/m²)']
            return irradiancia, temperatura
        except IndexError:
            print(f'No se encontraron datos de temperatura para {fecha_hora_str}')

    def buscar_irradiancia_temperatura_rango(self, tupla_inicio, tupla_fin):
        fecha_hora1_str = f'{tupla_inicio[0]:02d}-{tupla_inicio[1]:02d}-2019 {tupla_inicio[2]:02d}:{tupla_inicio[3]:02d}'
        fecha_hora2_str = f'{tupla_fin[0]:02d}-{tupla_fin[1]:02d}-2019 {tupla_fin[2]:02d}:{tupla_fin[3]:02d}'
        try:
            datos_rango = self.df[(self.df['Fecha'] >= fecha_hora1_str) & (self.df['Fecha'] <= fecha_hora2_str)]
            resultados = []
            for _, fila in datos_rango.iterrows():
                temperatura = fila['Temperatura (°C)']
                irradiancia = fila['Irradiancia (W/m²)']
                tupla_irrad_temp = (irradiancia, temperatura)
                resultados.append(tupla_irrad_temp)

            return resultados
        except IndexError:
            print('No se encontraron datos en el rango de fechas proporcionado')

# Ejemplo de uso
datos_climatologicos = DatosClimatologicos('Datos_climatologicos_Santa_Fe_2019.xlsx')

# Buscar datos para una fecha específica
tupla_fecha = (4, 1, 18, 20)
resultado_fecha = datos_climatologicos.buscar_irradiancia_temperatura(tupla_fecha)
print('Datos para la fecha:')
print(resultado_fecha)

# Buscar datos en un rango de fechas
tupla_inicio = (4, 1, 18, 20)
tupla_fin = (4, 2, 8, 40)
resultados_rango = datos_climatologicos.buscar_irradiancia_temperatura_rango(tupla_inicio, tupla_fin)
print('Rango de la tabla:')
for resultado in resultados_rango:
    print(resultado)




def graficar_pot_rango(tupla1, tupla2, N, Ppico, eta, kp, Pinv, archivo_excel, mu=2, Gstd=1000, Tr=25):


    df = pd.read_excel(archivo_excel)

  
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df_filtrado = df[(df['Fecha'] >= pd.to_datetime(tupla1)) & (df['Fecha'] <= pd.to_datetime(tupla2))]

    if df_filtrado.empty:
        print("No hay datos para el rango de tiempo especificado.")
        return

  
    potencias_generadas = []
    fechas = []

    for _, fila in df_filtrado.iterrows():
        G = fila['Irradiancia (W/m²)']
        T = fila['Temperatura (°C)']

      
        Ncorr = N * (G / Gstd) * (1 + kp * ((T - Tr) / 100))

   
        Pmodelo = Ncorr * Ppico * (1 - mu * ((T - Tr) / 100)) * eta / 100

   
        Pmodelo = min(Pmodelo, Pinv)

        potencias_generadas.append(Pmodelo)
        fechas.append(fila['Fecha'])

  
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, potencias_generadas, label='Potencia Generada')
    plt.title('Potencia Generada por el Sistema Fotovoltaico')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Potencia Generada (W)')
    plt.legend()
    plt.grid(True)
    plt.show()


tupla_inicio = ('2019-04-01 07:00:00')
tupla_fin = ('2019-04-04 20:00:00')
eficiencia_nominal_modulo = 18  # %
potencia_pico_modulo = 300  # W
eficiencia_inversor = 95  # %
factor_perdida = 0.02  # %
potencia_nominal_inversor = 5000  # W
archivo_excel = 'Datos_climatologicos_Santa_Fe_2019.xlsx'

graficar_pot_rango(tupla_inicio, tupla_fin, eficiencia_nominal_modulo, potencia_pico_modulo,
                   eficiencia_inversor, factor_perdida, potencia_nominal_inversor, archivo_excel)

