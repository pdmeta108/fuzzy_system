import csv
import os
from re import search
from FuzzyVariableClass import FuzzyVariable
from FCLParser.fcl_parser import FCLParser


class FuzzySystem:
    def obtener_set(self, set_nombre, tipo, file):

        try:
            with open(file) as csv_file:
                file_open = csv.reader(csv_file, delimiter=',')
        except Exception as e:
            return print(e)

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            x_variable = []
            set_variable = []
            line_count = 0
            for row_set in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                fuzzy_set = FuzzyVariable(row_set[0], row_set[1], int(row_set[2]), int(row_set[3]), set_nombre)
                if search(set_nombre, row_set[0]) and search(tipo, row_set[-1]):
                    if row_set[1] == "triangular":
                        x_set, var_set = FuzzyVariable.crear_set_triangular(fuzzy_set, int(row_set[4]), int(row_set[5]), int(row_set[6]))
                    elif row_set[1] == "trapezoidal":
                        x_set, var_set = FuzzyVariable.crear_set_trapezoidal(fuzzy_set, int(row_set[7]), int(row_set[8]), int(row_set[9]), int(row_set[10]))
                    else:
                        line_count += 1
                        continue
                    x_variable.append(x_set)
                    set_variable.append(var_set)
                line_count += 1
            return x_variable, set_variable

    def obtener_FCL(self, file):
        p = FCLParser()

        try:
            with open(file) as fcl_file:
                infile = os.path.join(os.path.dirname(os.path.realpath(__file__)), file)
                p.read_fcl_file(infile)
        except Exception as e:
            return print(e)

        infile = os.path.join(os.path.dirname(os.path.realpath(__file__)), file)
        return infile
