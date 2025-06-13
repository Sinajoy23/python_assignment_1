# Task 1 
# greet_user
def greet_user(name):
    """Display a simple greeting."""
    print(f"Hello, {name.title()}!")
#add_numbers
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b
# Main script            

greet_user("Pamela")
add_numbers(5, 10)

# Task 2

pet_name = "Buddy"
def describe_pet(name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}.")

# Call the function 
describe_pet("Whiskers", "cat")
describe_pet("Buddy")  # uses value "dog"
print("")
print("")

def make_sandwich(*ingredients):
    """Make a sandwich with variable ingredients."""
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Task 3

make_sandwich("Turkey", "Lettuce", "Tomato")
make_sandwich("Peanut Butter", "Jelly") 
make_sandwich("Lettuce", "Tomato", "Cheese")
print("")
print("")

# Task 4
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test them
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")