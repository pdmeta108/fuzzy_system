import csv
from re import search
from FuzzyVariableClass import FuzzyVariable


class FuzzySystem:
    def obtener_set(self, set_nombre, file):

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
                if search(set_nombre, row_set[0]):
                    if row_set[1] == "triangular":
                        x_set, var_set = FuzzyVariable.crear_set_triangular(fuzzy_set, int(row_set[4]), int(row_set[5]), int(row_set[6]))
                    elif row_set[1] == "trapezoidal":
                        x_set, var_set = FuzzyVariable.crear_set_trapezoidal(fuzzy_set, int(row_set[7]), int(row_set[8]), int(row_set[9]), int(row_set[10]))
                    else:
                        continue
                    x_variable.append(x_set)
                    set_variable.append(var_set)
                line_count += 1
            return x_variable, set_variable
