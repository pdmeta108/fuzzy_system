# Clase variable difusa
import csv
import numpy as np
import skfuzzy as fuzz
from re import search


class FuzzySet:
    def __init__(self, nombre, tipo, funcion, min, max):
        self.nombre = nombre
        self.tipo = tipo
        self.funcion = funcion
        self.min = min
        self.max = max


class FuzzyVariable(FuzzySet):

    def __init__(self, nombre, min, max, set_nombre):
        super().__init__(nombre, min, max)
        self.set_nombre = set_nombre

    def crear_set_triangular(self, a, b, c):
            x_tr = np.arange(self.min, self.max + 1, 1)
            var_tr = fuzz.trimf(x_tr, [a, b, c])
            return x_tr, var_tr

    def crear_set_trapezoidal(self, a, b, c, d):
            x_trap = np.arange(self.min, self.max + 1, 1)
            var_trap = fuzz.trapmf(x_trap, [a, b, c, d])
            return x_trap, var_trap

    def union(self,set_l, set_r):
        return  np.fmin(set_l, set_r)

    def interseccion(self, set_l, set_r):
        return np.fmax(set_l, set_r)

    def obtener_set(self, set_nombre, file):
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            x_variable = []
            set_variable = []
            line_count = 0
            for row_set in csv_reader:
                if search(set_nombre, row_set[0]):
                    if row_set[2] == "triangular":
                        x_set, var_set = self.crear_set_triangular(row_set[4], row_set[5], row_set[6])
                    elif row_set[2] == "trapezoidal":
                        x_set, var_set = self.crear_set_trapezoidal(row_set[7], row_set[8], row_set[9], row_set[10])
                    else:
                        continue
                    x_variable.append(x_set)
                    set_variable.append(var_set)
                line_count += 1
            return x_variable, set_variable

