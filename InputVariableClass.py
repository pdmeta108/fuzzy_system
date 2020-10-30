from .FuzzyVariableClass import FuzzyVariable
import skfuzzy as fuzz


class InputFuzzyVariable(FuzzyVariable):

    def fusificar(self, set_nombre, valor):
        fuzzy_x = []
        x_set, var_set = self.obtener_set(set_nombre, 'input_set_data.csv')
        for y in var_set:
            fuzzy_x.append(fuzz.interp_membership(x_set[0], y, valor))
        return fuzzy_x



