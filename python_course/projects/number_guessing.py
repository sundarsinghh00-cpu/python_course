import random

secret_number = random.randint(1, 30)
attempts = 0
max_attempts = 5

print("Welcome to number guessing game!")
print(f"Guess a number between 1 to 30. You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number: 
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break

if guess != secret_number:
    print(f"Sorry, you lost. The number was {secret_number}.")

