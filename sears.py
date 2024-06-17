# The following code fragment contains code from the Sears tower problem.
#  It also has a bug in it.
# Identify the error and fix it.

# sears.py

# bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
# sears_height   = 442             # Height (meters)
# num_bills      = 1
# day            = 1

# while num_bills * bill_thickness < sears_height:
#     print(day, num_bills, num_bills * bill_thickness)
#     day = days + 1
#     num_bills = num_bills * 2

# print('Number of days', day)
# print('Number of bills', num_bills)
# print('Final height', num_bills * bill_thickness)

# solution:
# error in line 14
# days is not defined
# use 'day' insted

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)