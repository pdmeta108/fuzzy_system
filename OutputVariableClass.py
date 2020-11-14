from FuzzyVariableClass import FuzzyVariable
import skfuzzy as fuzz
import numpy as np


class OutputFuzzyVariable(FuzzyVariable):
    def __init__(self, nombre, min, max, set_nombre):
        super().__init__(nombre, min, max)
        self.distribucion = FuzzyVariable(nombre, min, max, set_nombre)

    def obtener_salida(self, set_nombre, regla_consecuente, tipo_set):
        dfuzzy_x = []
#        x_set, var_set = self.obtener_set(set_nombre, 'output_set_data.csv')
#        for y in regla_consecuente:
#            dfuzzy_x.append(np.fmin(var_set[tipo_set - 1], y))
#        return dfuzzy_x, x_set

    def defusificar(self, agregado, x_salida):
        return fuzz.defuzz(x_salida, agregado, 'centroid')


