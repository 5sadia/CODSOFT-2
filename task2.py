def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Select operation to be performed:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    op_choice = input("Enter your choice (1,2,3,4): ")

    if op_choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if op_choice == '1':
            print("Result: ", add(number1, number2))
        elif op_choice == '2':
            print("Result: ", sub(number1, number2))
        elif op_choice == '3':
            print("Result: ", multiply(number1, number2))
        elif op_choice == '4':
            print("Result: ", div(number1, number2))
        break
    else:
        print("Invalid Input")
