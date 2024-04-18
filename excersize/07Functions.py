def divide(numerator, denominator):

  try:
    return numerator / denominator
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    return None

numerator = float(input("First Number: "))
denominator = float(input("Second Number: "))
result = divide(numerator, denominator)

if result is not None:
  print(f"The result of dividing is: {result}")

