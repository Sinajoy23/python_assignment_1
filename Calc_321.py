import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

print("My Error 🎯 Spotter Calculator 😊!")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("bye! ttyl...")
        break
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"The result is: {result}")
                break
            elif choice == '2':
                result = num1 - num2
                print(f"The result is: {result}")
                break
            elif choice == '3':
                result = num1 * num2
                print(f"The result is: {result}")
                break
            elif choice == '4':
                if num2 == 0:
                    logging.error("ZeroDivisionError occurred: division by zero")
                    print("Uh oh! Division by zero ❌ is not permitted")
                else:
                    result = num1 / num2
                    print(f"The result is: {result}")
                    
        except ValueError as e:
            logging.error(f"ValueError occurred: {e}")
            print("Bad input! Enter a valid number.")
    else:
        print("Bad input! Enter a valid number.")

print("Thanks for using my error spotter calculator 😊✨!")