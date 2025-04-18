class Calc:
    def __init__(self):
        print("Default")

    def sum(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


O1 = Calc()
n1 = float(input("Enter the value of number 1: "))
n2 = float(input("Enter the value of number 2: "))
output_sum = O1.sum(n1, n2)
output_sub = O1.sub(n1, n2)
output_mul = O1.mul(n1, n2)
output_div = O1.div(n1, n2)

print(output_sum, output_sub, output_mul, output_div)