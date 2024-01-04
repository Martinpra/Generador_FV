import pandas as pd
from Generador_FV import Generador_FV  # Asegúrate de importar la clase Generador_FV desde su módulo

class Generador_FV_Sta_Fe(Generador_FV):
    def __init__(self, N, Ppico, eta, kp, Pinv, mu=2, Gstd=1000, Tr=25):
        # Llamada al método de inicialización de la clase base
        super().__init__(None, N, Ppico, eta, kp, Pinv, mu, Gstd, Tr)
        
        # Cargar los datos meteorológicos de Santa Fe desde el archivo Excel
        self.tabla_anual = self.cargar_datos_santa_fe()

    def cargar_datos_santa_fe(self):
        ruta_archivo_santa_fe = 'Datos_climatologicos_Santa_Fe_2019.xlsx'
        datos_santa_fe = pd.read_excel(ruta_archivo_santa_fe)
        # Asegúrate de tener las columnas adecuadas en tu archivo Excel
        return datos_santa_fe[['Irradiancia', 'Temperatura']]

# Ejemplo de uso
generador_santa_fe = Generador_FV_Sta_Fe(N=12, Ppico=240, eta=0.97, kp=-0.0044, Pinv=2.5)
print(generador_santa_fe)
print(generador_santa_fe.Gstd)
print(generador_santa_fe.Tr)
