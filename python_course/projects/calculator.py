def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "cannot divide by zero"

# Calculator starts here (NOT indented)
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("choose operation (+,-,*,/): ")

if operation == "+":
    print("result:", add(num1, num2))
elif operation == "-":
    print("result:", subtract(num1, num2))
elif operation == "*":
    print("result:", multiply(num1, num2))
elif operation == "/":
    print("result:", divide(num1, num2))
else:
    print("invalid operation")
