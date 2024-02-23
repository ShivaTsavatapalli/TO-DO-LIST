def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter first 3 letters : ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'add':
        print("Result:", add(num1, num2))
    elif choice == 'sub':
        print("Result:", subtract(num1, num2))
    elif choice == 'mul':
        print("Result:", multiply(num1, num2))
    elif choice == 'div':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

calculator()
