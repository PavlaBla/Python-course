import csv

# Tuples look like read-only lists. However, tuples are most often used 
# for a single item consisting of multiple parts. Lists are usually 
# a collection of distinct items, usually all of the same type.

# packing and unpacking of tuples
s = ('GOOG', 100, 490.1)

name, shares, price = s
# The number of variables on the left must match the tuple structure.
print('Cost', shares * price)

# dictionaries
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

# To get values from a dictionary use the key names.
print(s['name'], s['shares'])

# To add or modify values assign using the key names.
s['shares'] = 75
s['date'] = '6/6/2024'

print(s['shares'], s['date'])

# To delete a value use the del statement.
del s['date']

# using tuples or dictionaries to work with data:

with open ('portfolio.csv', mode= 'r', encoding= 'utf-8') as f:
    rows = csv.reader(f)
    print(next(rows))
    row = next(rows)
    print(row)

# just like this, we can't perform any operations
# hence we can use tuples:

t = (row[0], int(row[1]), float(row[2]))
print(t)

cost = t[1] * t[2]
print(cost)
# or to print two decimals only:
print(f'{cost:0.2f}') 

# to change tuple content, you have to create a new one:
t = (t[0], 75, t[2])

name, shares, price = t
print(name)
print(shares)
print(price)

# we can do mathematical operations and pack the values
# back to tuple

t = (name, 2* shares, price)
print(t)

# dictionaries
d = {
    'name' : row[0],
    'shares' : int(row[1]),
    'price' : float(row[2])
}

print(d)

# Calculate the total cost of this holding:
cost = d['shares'] * d['price']
print(cost)

# dictionaries can be modified
d['shares'] = 75
d['date'] = (6, 11, 2024)
d['account'] = 12345

print(d)

# If you turn a dictionary into a list, you’ll get all of its keys:
print(list(d))

# Similarly, if you use the for statement to iterate on a dictionary,
# you will get the keys:
for k in d:
    print('k =', k)

# Try this variant that performs a lookup at the same time:
for k in d:
    print(k , '=', d[k])

# You can also obtain all of the keys using the keys() method:
keys = d.keys()
print(keys)

# This is an overlay on the original dictionary that always gives 
# you the current keys—even if the dictionary changes. For example, try this:
del d['account']
print(keys)

# items method gives us (key, value) tuple
items = d.items()
print(items)

for k, v in d.items():
    print(k, '=', v)

d = dict(items)
print(d)






