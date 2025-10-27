num1 = int(input("number1: "))
op = input("enter an operator: ")
num2 = int(input("number2: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("invalid operator")
print("continue")