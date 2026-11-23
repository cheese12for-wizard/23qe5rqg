# weight comverter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K / Lbs): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit}.")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "K"
    print(f"Your weight is {round(weight, 2)} {unit}.")
else:
    print(f"{unit} is not a unit!")

