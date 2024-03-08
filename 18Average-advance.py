def calculate_average_from_input():
    numbers = []
    while True:
        a = input("Enter a number (or 'done' to finish): ")
        if a.lower() == 'done':
            break
        else:
            try:
                number = float(a)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    if not numbers:
        return None 
    total = sum(numbers)
    average = total / len(numbers)
    return average


average_result = calculate_average_from_input()


if average_result is not None:
    print(f"The average is: {average_result}")
else:
    print("No valid numbers entered. Cannot calculate average.")
