# Prompt the user for their favorite color
favorite_color = input("What is your favorite color? ")

# Prompt the user for the number of pets
num_pets_str = input("How many pets do you have? ")

# Check if input is a valid number for pets
while not num_pets_str.isdigit():
  num_pets_str = input("Invalid input. Please enter the number of pets as a number: ")

# Convert input to integer
num_pets = int(num_pets_str)

# Ask the user if they are a student (boolean)
is_student = input("Are you a student (yes/no)? ").lower() == "yes"

# Print a summary
print(f"\nYour favorite color is {favorite_color}. (type: {type(favorite_color)})")
print(f"You have {num_pets} pets. (type: {type(num_pets)})")  
print(f"Are you a student? {is_student} . (type: {type(is_student)})")
