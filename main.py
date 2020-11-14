from FuzzySystem import FuzzySystem
from InputVariableClass import InputFuzzyVariable

fuzzy_system = FuzzySystem()

x_input, var_input = fuzzy_system.obtener_set("puntuacion", "input_set_data.csv")
ff = InputFuzzyVariable.fusificar(x_input, var_input, 70)
print(ff)
