# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of 
# $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin 
# trading corporation. The interest rate is 5% and the monthly 
# payment is $2684.11.
# Here is a program that calculates the total amount that Dave 
# will have to pay over the life of the mortgage:


initial = 500000
monthly = 2684.11
interest = 0.05

total_paid = 0.0

while initial > 0:
    initial = initial * (1+interest/12) - monthly
    total_paid = total_paid + monthly

print('Total paid', total_paid)

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the total 
# amount paid along with the number of months required.

initial = 500000
monthly = 2684.11
interest = 0.05
total_paid = 0.0
month = 0

extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 12

while initial > 0:
    initial = initial * (1+interest/12) - monthly
    total_paid = total_paid + monthly
    month += 1
    
    if extra_payment_start_month <= month and extra_payment_end_month >= month:
        initial = initial - extra_payment
        total_paid = total_paid + extra_payment
    print(month, round(total_paid,2), round(initial,2))

print('Total paid', round (total_paid,2))
print('Months', month)

# How much will Dave pay if he pays an extra $1000/month 
# for 4 years starting after the first five years have already been paid?

initial = 500000
monthly = 2684.11
interest = 0.05
total_paid = 0.0
month = 0

extra_payment = 1000
extra_payment_start_month = (5*12) + 1
extra_payment_end_month = (extra_payment_start_month + (4*12)) -1

while initial > 0:
    initial = initial * (1+interest/12) - monthly
    total_paid = total_paid + monthly
    month += 1
    
    if extra_payment_start_month <= month and extra_payment_end_month >= month:
        initial = initial - extra_payment
        total_paid = total_paid + extra_payment
    print(month, round(total_paid,2), round(initial,2))

print('Total paid', round (total_paid,2))
print('Months', month)

# Modify the program to print out a table showing the month,
# total paid so far, and the remaining balance. Make sure,
# there is no overpayment in the end.


initial = 500000
monthly = 2684.11
interest = 0.05
total_paid = 0.0
month = 0

extra_payment = 1000
extra_payment_start_month = (5 * 12) + 1  # Start extra payment after 5 years
extra_payment_end_month = (extra_payment_start_month + (4 * 12)) - 1  # End extra payment after 4 years

# Header for the table
print(f"{'Month':<6} {'Total Paid':<12} {'Remaining Balance':<16}") # means left alignment and number of spaces in a field

# Loop until the loan is paid off
while initial > 0:
    month += 1

    # Calculate interest for the month
    interest_for_month = initial * (interest / 12)
    initial += interest_for_month

    # Determine if an extra payment is applicable
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = monthly + extra_payment
    else:
        payment = monthly

    # Adjust payment if it exceeds the remaining balance
    if payment > initial:
        payment = initial

    # Subtract the payment from the balance
    initial -= payment
    total_paid += payment

    # Print the current state
    print(f"{month:<6} {round(total_paid, 2):<12} {round(initial, 2):<16}")

# Final outputs
print('Total paid:', round(total_paid, 2))
print('Months:', month)
