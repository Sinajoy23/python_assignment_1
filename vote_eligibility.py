# Step 1: Ask the Age
# Asking the user their age and convert it to an integer.
age = int(input("How old are you? "))

# Step 2: Decide the Eligibility
# Using a conditional statement (if/else) to check the age.
if age >= 18:
    # If the age is 18 or older, the user is eligible to vote.
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    # If the age is less than 18, how many years they need to wait.
    years_to_wait = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_to_wait} more years to go! Patience is a virtue.")

# Step 3: Experiment Test with Different Ages and Polish It Up
# Step 4: Add a Fun Twist
print("""You are a Rockstar!☆*: .｡. o(≧▽≦)o .｡.:*☆""")
print("Thank you for checking your voting eligibility! Remember, every vote counts, and your voice matters. Stay informed and engaged in your community!")