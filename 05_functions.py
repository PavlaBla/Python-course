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

for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:    #must match the kind of error we try to catch
        print("Couldn't parse", line)
    