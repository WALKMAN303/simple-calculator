num1 = float(input("Enter the 1st number: "))
op = input("Enter your wanted operator: ")
num2 = float(input("Enter the 2nd number: "))
op = input("Enter your wanted operator: ")
num3 = float(input("Enter the 3rd number: "))
op = input("Enter your wanted operator: ")
num4 = float(input("Enter the 4th number: "))


if op == "+":
    print(num1 + num2 + num3 + num4)
elif op == "-":
    print(num1 - num2 - num3 - num4)
elif op == "*":
    print(num1 * num2 * num3 * num4)
elif op == "/":
    print(num1 / num2 / num3 / num4)
else:
    print("Invalid operator")