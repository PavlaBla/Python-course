# 1.1
# Lucky Larry bought 75 shares of Google stock at a price of $235.14 per share. 
# Today, shares of Google are priced at $711.25. Using Python’s interactive mode 
# as a calculator, figure out how much profit Larry would make if he sold all of his shares

profit = 75 * (711.25-235.14)
print(profit)

# how much profit does Larry make after his evil broker takes their 20% cut?
after = profit * 0.80
print(after)

# 
# One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. 
# Each day thereafter, you go out double the number of bills. How long does it take for the stack 
# of bills to exceed the height of the tower?

bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills = num_bills * 2

print(f'number of bils = {num_bills}')
print(f'number of days = {day}')
print(f'total height = {num_bills * bill_thickness}')


# vytisteni na jeden radek - odstraneni newline
print('Hello', end=' ')
print('My name is', 'Jake')
