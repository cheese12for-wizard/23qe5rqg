operator = input("enter an operator ( + - * / ) here: ")
num1 = float(input("enter a nummber here: "))
num2 = float(input("enter a second number here: "))

if operator == "+":
    print(f"The total is {num1 + num2}")
elif operator == "-":
    print(f"The total is {num1 - num2}")
elif operator == "*":
    print(f"The total is {num1 * num2}")
elif operator == "/":
    print(f"The total is {num1 / num2}")
else:
    print("That is not a valid operator!")