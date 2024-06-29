# to sum first n integers:
def sumcount (n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(sumcount(4))

# Functions report errors as exceptions

# Exceptions can be caught and handled.
# To catch, use the try - except statement.

# for line in file:
#     fields = line.split(',')
#     try:
#         shares = int(fields[1])
#     except ValueError:    #must match the kind of error we try to catch
#         print("Couldn't parse", line)

# working with files
# we want to calculate total cost of shares based on the table portfolio.csv

total_cost = 0

with open ('portfolio.csv', mode= 'r', encoding= 'utf-8') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        cost = float(row[2])
        total_cost += shares * cost

print(f'Total cost {total_cost}')

# now do the same as a function:
def portfolio_cost(filename):

    total_cost = 0

    with open (filename, mode= 'r', encoding= 'utf-8') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            cost = float(row[2])
            total_cost += shares * cost
    return total_cost

cost = portfolio_cost('portfolio.csv')
print(f'Total cost {cost}')

# what happens if my file is missing some data
# cost = portfolio_cost('missing.csv')
# print(f'Total cost {cost}')

# modify the program to catch the exception, print a warning
# message, and continue processing the rest of the file.

def portfolio_cost(filename):
        with open (filename, mode= 'r', encoding= 'utf-8') as f:
            total_cost = 0
            headers = next(f)
            for line in f:
                row = line.split(',')
                if line:
                    try:
                        shares = int(row[1])
                        cost = float(row[2])
                        total_cost += shares * cost
                    except ValueError:
                        print(print("Couldn't parse", line))
            return total_cost


cost = portfolio_cost('missing.csv')
print(f'Total cost {cost}')

