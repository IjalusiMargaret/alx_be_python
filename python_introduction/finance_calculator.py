# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a 5% interest rate for the annual savings projection
interest_rate = 0.05

# Calculate the projected savings after one year, including interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")