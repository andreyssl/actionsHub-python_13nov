# ask user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ask user for operator
operator = input("Enter operator (+, -, *, /): ")

# calculate result
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

# print result
print(num1, operator, num2, "=", result)