# Open the file for writing in text mode (with error handling)
try:
  with open("data.txt", "w") as file:
    # Write numbers from 1 to 10 on separate lines
    for num in range(1, 11):
      file.write(f"{num}\n")  # Use f-string for newline character
  print("Numbers written to data.txt successfully.")
except OSError as e:
  print(f"Error writing to file: {e}")

# Open the file for reading in text mode (with error handling)
try:
  with open("data.txt", "r") as file:
    # Read and print the contents of the file
    contents = file.read()
    print("\nContents of data.txt:")
    print(contents)
except OSError as e:
  print(f"Error reading from file: {e}")
