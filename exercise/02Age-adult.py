# Get user's age
age_str = input("Enter your age Please: ")

# Check if input is a valid number
while not age_str.isdigit():
  age_str = input("Invalid input. Please enter your age as a number: ")

# Convert input to integer
age = int(age_str)

# Determine and print classification
if age < 18:
  print("You are a minor.")
else:
  print("You are an adult.")