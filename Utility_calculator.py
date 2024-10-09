class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b

# print(Calculator.add(12,17))
# print(Calculator.multiply(12, 17))

result_add = Calculator.add(12,17)
result_multiply = Calculator.multiply(12,17)

print(f"Addition Result: {result_add}")
print(f"Multiplication Result: {result_multiply} ")
