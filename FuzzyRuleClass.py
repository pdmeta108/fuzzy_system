import numpy as np
import skfuzzy as fuzz


class RuleClass:

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent