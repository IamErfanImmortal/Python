numbers_list = [10, 15, 20, 25, 30]


def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

average_result = calculate_average(numbers_list)

if average_result is not None:
    print(f"The average is: {average_result}")
else:
    print("The list is empty. Cannot calculate average.")

