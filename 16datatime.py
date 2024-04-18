from datetime import date

# Get today's date
today = date.today()

# Extract and print month and year
month_name = today.strftime("%B")  # Full month name (e.g., January)
year = today.year

print(f"Current month: {month_name}")
print(f"Current year: {year}")
