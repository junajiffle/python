age = input("What is your current age?")

remaining_years = 90 - int(age)

remaining_months = remaining_years * 12

remaining_weeks = remaining_years * 52

remaining_days = remaining_years * 365

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
