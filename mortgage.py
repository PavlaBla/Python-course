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
# total paid so far, and the remaining principal.

initial = 500000
monthly = 2684.11
interest = 0.05
total_paid = 0.0
month = 0
months_paid = 310

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while month < months_paid and initial > 0:
    month += 1
    interest_payment = initial * (interest / 12)
    principal_payment = monthly - interest_payment
    initial -= principal_payment
    total_paid += monthly

    if extra_payment_start_month <= month <= extra_payment_end_month:
        extra_payment = min(extra_payment, initial)  # Correct for overpayment
        initial -= extra_payment
        total_paid += extra_payment

    print(month, round(total_paid, 2), round(initial, 2))

# needs to be corrected!

