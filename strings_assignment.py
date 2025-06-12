# Task 1 - String Slicing and Indexing
statement = "Python is amazing!"

first_word = statement[:6]            # Characters 0 to 5
amazing_part = statement[10:17]       # Characters from "amazing"
reversed_statement = statement[::-1]   # Reverse string

print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_statement)
print("")
print("")
# Task 2 - Methods
statement_2 = " hello, python world! "

stripped1 = statement_2.strip()
capitalized = stripped1.capitalize()
replaced = stripped1.replace("world", "universe")
uppercased = stripped1.upper()

print("Stripped:", stripped1)
print("Capitalized:", capitalized)
print("Replaced:", replaced)
print("Uppercased:", uppercased)

print("")   
print("")

# Task 3 - Palindromes
word = input("Enter a word: ").lower()  # Lowercase for comparison
backwards_word = word[::-1]

if word == backwards_word:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Nope, '{word}' is not a palindrome.")

