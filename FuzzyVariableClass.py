# Clase variable difusa

from abc import ABC, abstractmethod
import numpy as np
import skfuzzy as fuzz


class FuzzySet(ABC):
    def __init__(self, nombre, funcion, min, max):
        self.nombre = nombre
        self.funcion = funcion
        self.min = min
        self.max = max


class FuzzyVariable(FuzzySet):

    def __init__(self, nombre, funcion, min, max, set_nombre):
        super().__init__(nombre, funcion, min, max)
        self.set_nombre = set_nombre

    def crear_set_triangular(self, a, b, c):
            x_tr = np.arange(self.min, self.max + 1, 1)
            var_tr = fuzz.trimf(x_tr, [a, b, c])
            return x_tr, var_tr

    def crear_set_trapezoidal(self, a, b, c, d):
            x_trap = np.arange(self.min, self.max + 1, 1)
            var_trap = fuzz.trapmf(x_trap, [a, b, c, d])
            return x_trap, var_trap



