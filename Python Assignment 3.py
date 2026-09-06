# Number Guessing Game

import random
# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

attempts = 3
while attempts > 0:
    
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    if guess > secret_number:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")

   
    attempts -= 1
else:
    print("Game over! Better luck next time!")
    
    
    
       
    
# Multiplication Table Generator

# Ask the user to Enter a Number
number = int(input("\nEnter the number for which you want the Multiplication Table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
    
    
    
       
    
# BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your Weight in Kg: "))
height = float(input("Enter your Height in Meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")