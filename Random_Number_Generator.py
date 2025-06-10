import random
number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")        
print("Try to guess it in as few attempts")
print("as possible. Type 'exit' to quit the game.")
print(" ")
print("I'm thinking of a number between 1 and 100.")

# Track the number of guesses
attempts = 0
max_attempts = 10

# Start the loop
while attempts <= max_attempts:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess > number_to_guess:
        print("Too high! Try again.\n")
    elif guess < number_to_guess:
        print("Too low! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
else:
    print(f"Game has ended! The number was {number_to_guess}. Better luck next time!")

