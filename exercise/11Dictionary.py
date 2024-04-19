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

# Print the updated student information
print("\nUpdated student information:")
print(student)


