def show_menu(): # Start of show_menu function
    print("Welcome to the Art for recursion Program!")
    print("Choose an option below:")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Draw a Recursive Fractal")
    print("4. Exit")
# end of show_menu function
def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
        # end of factorial function
def handle_factorial():
    num = int(input("Enter a number to find its factorial: "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        print(f"The factorial of {num} is {factorial(num)}.")
    # end of handle_factorial function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    # end of fibonacci function
def handle_fibonacci():
        num = int(input("Enter a number to find its Fibonacci: "))
        if num < 0:
            print("Please enter a positive integer.")
        else:
            print(f"The Fibonacci of {num} is {fibonacci(num)}.")
    # end of handle_fibonacci function
    
import turtle

# Recursive function to draw a fractal tree 🌳
def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Function to set up the turtle window and for the drawing to start
def handle_fractal():
    window = turtle.Screen()
    window.title("Tree Drawing") 
    t = turtle.Turtle()
    t.left(90)  
    t.speed("fast") 
    draw_tree(100, t)
    window.bye()  # Closes the window when done

def main(): #start of main function
    # This is the main function that runs the Menu program
    while True:
        show_menu()
        choice = input("> ")

        if choice == '1':
            handle_factorial()
        elif choice == '2':
            handle_fibonacci()
        elif choice == '3':
            handle_fractal()
        elif choice == '4':
            print("Goodbye Y'all!💕")
            break
        else:
            print("Please choose a valid option (1,2,3, or 4).")

# This will start the program
main()


