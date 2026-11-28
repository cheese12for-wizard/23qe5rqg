# weight comverter

unit = input("Kilograms or pounds? (K / Lbs): ").lower()
weight = float(input("Enter your weight: "))

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight, 2)} {unit}.")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "k"
    print(f"Your weight is {round(weight, 2)} {unit}.")
else:
    print(f"{unit} is not a unit!")

