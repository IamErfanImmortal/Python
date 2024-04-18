# Get the temperature (can replace with actual temperature reading)
while True:
  try:
    temperature = float(input("Enter the temperature: "))
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a number for the temperature.")

if temperature > 30:
  print("It's hot!")
elif temperature >= 20:
  print("It's nice.")
else:
  print("It's cold.")

