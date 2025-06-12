# Password Strength Checker 🔐

# Step 1 - Ask for a password
password = input("💼    Enter your password: ")

# Step 2 - Evaluate the given password
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "@#$%^&*!?" for char in password)

# Step 3 - Check against each rule
issues = []

if not length_ok:
    issues.append("at least 8 characters")
if not has_upper:
    issues.append("one uppercase letter")
if not has_lower:
    issues.append("one lowercase letter")
if not has_digit:
    issues.append("one digit")
if not has_special:
    issues.append("one special character (@, #, $, etc.)")

# Show results
if not issues:
    print("✅✅✅ Your password is strong! 💪")
else:
    print("⚠️   Your password needs:", ", ".join(issues) + ".")

# Bonus - Password Strength Meter
strength = 0
if length_ok: strength += 2
if has_upper: strength += 2
if has_lower: strength += 2
if has_digit: strength += 2
if has_special: strength += 2

print(f"Password strength: {strength}/10")
