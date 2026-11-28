unit = input("Celsius or fahrenheit (c / f): ".lower())
temp = float(input("Enter a temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32, 1)
    print(f"Your temperature is {temp}°F.")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"Your temperature is {temp}°C.")
else:
    print(f"{unit} is not a valid unit!") 