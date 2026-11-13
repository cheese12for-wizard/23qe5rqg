import random
number = random.randint(1, 100)

guess = 0

print("guess the number between 1 and 100!")

while guess != number:
    guess = int(input("your guess: "))

    if guess < number:
        print("higher")
    elif guess > number:
        print("lower")
    else:
        print("correct")