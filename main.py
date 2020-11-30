import os
from FCLParser.fcl_parser import FCLParser
from FuzzySystem import FuzzySystem
from InputVariableClass import InputFuzzyVariable

fuzzy_system = FuzzySystem()
p = FCLParser()
# FCL input file is in the same directory as this script:
infile = fuzzy_system.obtener_FCL("rule_system.fcl")
p.read_fcl_file(infile)


x_input, var_input = fuzzy_system.obtener_set("puntuacion", "entrada", "input_set_data.csv")
ff = InputFuzzyVariable.fusificar(x_input, var_input, 70)
print(p.rules)
