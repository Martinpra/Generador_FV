import numpy as np

class Generador_FV:
    def __init__(self, tabla_anual, N, Ppico, eta, kp, Pinv, mu=2, Gstd=1000, Tr=25):
        self.N = N
        self.Ppico = Ppico
        self.eta = eta
        self.kp = kp
        self.Pinv = Pinv
        self.mu = mu
        self._Gstd = Gstd
        self._Tr = Tr
        self.tabla_anual = tabla_anual

    @property
    def Gstd(self):
        return self._Gstd

    @property
    def Tr(self):
        return self._Tr
    
    def __str__(self):
        return f"Generador fotovoltaico con {self.N} paneles de {self.Ppico} W-pico"

    def __repr__(self):
        return f"<Generador FV: N={self.N}, Ppico={self.Ppico}, eta={self.eta}, kp={self.kp}, Pinv={self.Pinv}, mu={self.mu}>"

    def irrad_temp(self, d, m, h, mi):
        # Implementar lógica para obtener irradiancia y temperatura para un momento dado
        pass

    def irrad_temp_rango(self, tupla1, tupla2):
        # Implementar lógica para obtener irradiancia y temperatura en un rango de momentos
        pass

    def pot_modelo_GFV(self, G, T):
        # Implementar lógica para calcular la potencia generada por el GFV con los datos indicados
        pass

    def pot_generada(self, tupla_instante):
        # Implementar lógica para obtener la potencia generada en un instante dado
        pass

    # Otros métodos relacionados con el generador fotovoltaico

# Ejemplo de uso
# Supongamos que tienes una tabla_anual, puedes proporcionarla al crear una instancia de Generador_FV
# tabla_anual = ... # tus datos
# generador = Generador_FV(tabla_anual, N=12, Ppico=240, eta=0.97, kp=-0.0044, Pinv=2.5)
# print(generador)
# print(generador.Gstd)
# print(generador.Tr)
# generador.irrad_temp(1, 1, 12, 0)  # Ejemplo de llamada a uno de los métodos
