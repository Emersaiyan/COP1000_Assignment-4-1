# Prompt user to enter employee's name, number of shifts, number of transactions, and transaction dollar value
employee_name = input("Enter employee's name: ")
num_shifts = int(input("Enter number of shifts: "))
num_transactions = int(input("Enter number of transactions: "))
transaction_value = float(input("Enter transaction dollar value: "))

# Calculate productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Initialize bonus variable
bonus = 0

# Determine bonus based on productivity score
if productivity_score <= 30:
    bonus = 50.00
elif productivity_score <= 69:
    bonus = 75.00
elif productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Output the employee's name and bonus
print(f"{employee_name}'s bonus is ${bonus:.2f}")
