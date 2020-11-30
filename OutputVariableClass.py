from FuzzyVariableClass import FuzzyVariable, FuzzySet
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class OutputFuzzyVariable(FuzzyVariable):

    def distribucion(self, rango, nombre):
        return ctrl.Consequent(rango, nombre)

    def defusificar(self, agregado, x_salida):
        return fuzz.defuzz(x_salida, agregado, 'centroid')


