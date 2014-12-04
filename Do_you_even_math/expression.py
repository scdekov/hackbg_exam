class Expression:
    def __init__(self, firs_operand, second_operand, operator):
        self.firs_operand = int(firs_operand)
        self.second_operand = int(second_operand)
        self.operator = operator

    def value(self):
        if self.operator == '+':
            return self.firs_operand + self.second_operand
        elif self.operator == '-':
            return self.firs_operand - self.second_operand
        elif self.operator == '*':
            return self.firs_operand * self.second_operand
        elif self.operator == '/':
            return self.firs_operand / self.second_operand
        elif self.operator == '^':
            return self.firs_operand ** self.second_operand

    def __str__(self):
        return "What is the answer to {} {} {}? >".format(self.firs_operand, self.operator, self.second_operand)

