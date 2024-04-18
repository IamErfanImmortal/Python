# Create a list to store the square numbers
square_numbers = []

# Calculate and append the first 10 square numbers
for i in range(1, 11):
  square_numbers.append(i * i)

# Print each square number with even/odd indication
for number in square_numbers:
  # Check if even using the modulo operator
  if number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f"{number} is odd")
