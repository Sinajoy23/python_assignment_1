# Task 1: Counting Down with Loops
print("Task 1:Countdown Timer\n")

# Ask the user for a starting number

start_number = int(input("Enter the starting number for countdown: "))
print("\n")
if start_number < 1:
    print("Please enter a starting number.")
else:
    # Use a while loop to print numbers down to 1
    current_number = start_number
    while current_number >= 1:
        print(current_number, end=" ") # Use end=" " to print on the same line
        current_number -= 1 

    # When the countdown ends, print a celebratory message
    print("\nBoom! Blast off! 🛸")

print("\n") # Add a newline for better separation between tasks


# Task 2: Multiplication Table
print("Task 2: Multiplication Table\n")

# Ask the user to input a number

num_for_table = int(input("Enter a number (then see its multiplication table 1 to 10): "))

    # Use a for loop to print the multiplication table for that number (from 1 to 10)
for i in range(1, 11): # range(1, 11) generates numbers from 1 up to (but not including) 11
    result = num_for_table * i
    print(f"{num_for_table} x {i} = {result}")

print("\n") # Add a newline for better separation


# --- Task 3: Find the Factorial ---
print("Task 3: Calculate Factorial")

# Ask the user for a number

factorial_number = int(input("Enter a number: "))
    
if factorial_number < 0:
        print("Factorial is not defined for negative numbers.")
elif factorial_number == 0:
        print("The factorial of 0 is 1.")
else:
    # Use a for loop to calculate the factorial
    factorial_result = 1 # Initialize factorial_result to 1 
    for i in range(1, factorial_number + 1): # Loop from 1 up to the number
        factorial_result *= i # Multiply factorial_result by the current number (i)

    # Print the result 
    print(f"The factorial of {factorial_number} is {factorial_result}.")