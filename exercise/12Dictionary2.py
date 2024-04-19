# Define a student dictionary
student = {
  "student_id": 12345,
  "name": "Alice Smith",
  "major": "Computer Science"
}

# Print the original student information
print("Original student information:")
print(student)

# Get the new major from the user
new_major = input("Enter the new major: ")

# Update the major in the dictionary
student["major"] = new_major

# Get the grade average from the user (assuming float)
while True:
  try:
    grade_average = float(input("Enter the student's grade average (float): "))
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a number for the grade average.")

# Add the grade average to the dictionary
student["grade_average"] = grade_average

# Print the updated student information
print("\nUpdated student information:")
print(student)
