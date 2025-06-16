# Task 1 
# This script demonstrates exception handling in Python.
# It includes examples of ZeroDivisionError, ValueError, IndexError, KeyError, and TypeError.
try:
    number = int(input("Enter a number, please: "))
    result = 100 / number
    print(f"100 divided by {number} is {result}.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Incorrect! ❌ Please enter a valid number.")

print("\n")
print("")
print("")
# Task 2
# This script demonstrates various exceptions in Python.
# It includes examples of IndexError, KeyError, and TypeError.
print("\nTask 2: Demonstrate Common Exceptions\n")

# IndexError example
try:
    numbers = [1, 2, 3]
    print(numbers[5])  # Index 5 does not exist
except IndexError:
    print("IndexError has occurred! List index is out of range. Please try a different index.")

# KeyError example
try:
    info = {"name": "Alice"}
    print(info["age"])  # 'age' does not exist
except KeyError:
    print("KeyError occurred! 🔑 Key was not found in the dictionary.")

# TypeError example
try:
    result = "5" + 3  # Invalid operation
except TypeError:
    print("TypeError occurred! Unable to add string and integer.")


print("\n")
print("")
print("")

# Task 3
# This script demonstrates a try-except-else-finally block in Python.
# It handles division by zero and invalid input types.
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
except ZeroDivisionError:
    print("You can't divide by zero!❌")
except ValueError:
    print("Please enter valid numbers.❌")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
