print("0 = Single")
print("1 = Married Filing Jointly")
print("2 = Married Filing Separately")
print("3 = Head of Household")

status = input("Enter filing status (0-3): ")
income = input("Enter taxable income: ")

# Validate filing status
if not status.isdigit():
    print("Error: filing status must be a number")
    quit()

# Validate income
try:
    income = float(income)
except:
    print("Error: income must be a number")
    quit()

status = int(status)

if status == 0:  # Single
    limits = [8350, 33950, 82250, 171550, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33]

elif status == 1:  # Married Filing Jointly
    limits = [16700, 67900, 137050, 208850, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33]

elif status == 2:  # Married Filing Separately
    limits = [8350, 33950, 68525, 104425, 186475]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33]

elif status == 3:  # Head of Household
    limits = [11950, 45500, 117450, 190200, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33]

else:
    print("Invalid filing status")
    quit()

tax = 0
previous_limit = 0

# Calculate tax progressively
for i in range(len(limits)):
    if income > limits[i]:
        tax += (limits[i] - previous_limit) * rates[i]
        previous_limit = limits[i]
    else:
        tax += (income - previous_limit) * rates[i]
        break

# Tax income above highest bracket
if income > previous_limit:
    tax += (income - previous_limit) * 0.35

print("Total tax owed:", round(tax, 2))
