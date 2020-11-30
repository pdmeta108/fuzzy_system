class RuleClass:

    def __init__(self, antecedents, consequents):
        self.antecedents = antecedents
        self.consequents = consequents

    @staticmethod
    def get_antecedents(self, rule):
        return rule.ControlSystem.antecedents

    @staticmethod
    def get_consequents(self, rule):
        return rule.ControlSystem.consequents


