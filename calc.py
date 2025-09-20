class Calculator:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error! Division by zero."
        return self.num1 / self.num2


print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

calc = Calculator(a, b) 

if choice == '1':
    print("Result:", calc.add())
elif choice == '2':
    print("Result:", calc.subtract())
elif choice == '3':
    print("Result:", calc.multiply())
elif choice == '4':
    print("Result:", calc.divide())
else:
    print("Invalid Input")
