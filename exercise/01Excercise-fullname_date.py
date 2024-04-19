from datetime import date

# Prompt the user for their full name
full_name = input("Enter your full name: ")

# Get today's date
today = date.today()

# Print the formatted output
print(f"Your name is: {full_name}, and today's date is: {today.strftime('%Y-%m-%d')}")
