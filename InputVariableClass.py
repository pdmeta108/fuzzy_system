from FuzzyVariableClass import FuzzyVariable
import skfuzzy as fuzz


class InputFuzzyVariable(FuzzyVariable):

    @staticmethod
    def fusificar(x_set, var_set, valor):
        fuzzy_x = []
        for y in var_set:
           fuzzy_x.append(fuzz.interp_membership(x_set[0], y, valor))
        return fuzzy_x


