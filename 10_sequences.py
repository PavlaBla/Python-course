import csv
import pprint

# # On lists, slices can be reassigned and deleted.
# # reassignment:
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12,13]

# # deletion:
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]
print(a)

# # break statement: to exit the loop and move on to other statement:
namelist = []
for name in namelist:
    if name == 'Jake':
        break

# # continue statement: to skip one element and move on to the next:
lines = []
for line in lines:
    if line == '\n':    # Skip blank lines
        continue

# # looping over inteegers:
# # The syntax is range([start,] end [,step]). start and step are optional, default is 0 and 1
for k in range(10, 50, 2):
    print(k)

# # enumerate function - adds an extra counter value to iteration.
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    print(i,name)

# # You can iterate with multiple iteration variables. Each tuple is 
# # unpacked into a set of iteration variables. The number of variables 
# # must match the number of items in each tuple.
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    print(x,y)

# # Zip function takes multiple sequences and makes an iterator that combines them.
# # A common use of zip is to create key/value pairs for constructing dictionaries.
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)

# # to get the values, you have to iterate
for column, value in pairs:
    print(column, value)

# # basic counting examples:
for n in range (10):
    print(n, end=' ') # prints on one line

for n in range (10, 0, -1):
    print(n, end= ' ')

# looping over data:
data = [4, 9, 1, 25, 16, 100, 49]

for x in data:
    print(x)

for n,x in enumerate(data):
    print(n,x)

# missing.csv contains data for a stock portfolio, but has some 
# rows with missing data. Using enumerate(), modify your pcost.py 
# program so that it prints a line number with the warning message 
# when it encounters bad input.

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
                 # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

# makes the script universal for different files 

cost = portfolio_cost(filename)
print('Total cost:', cost)

# In the file portfolio.csv, the first line contains
#  column headers. In all previous code, we’ve been discarding them.
# First try this to pair the file headers with a row of data using zip:


with open('portfolio.csv', mode= 'r', encoding='utf-8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    
    my_list = list(zip(headers, row))
    print(list)
    record = dict(zip(headers, row))
    print(record)

# This transformation is one of the most useful tricks to know about when 
# processing a lot of data files. For example, suppose you wanted to make 
# the pcost.py program work with various input files, but without regard 
# for the actual column number where the name, shares, and price appear.

# try your portfolio_cost function on a completely different data file : portfoliodate.csv 
# As long as the file has the required columns, the code will work.

# inverting a dictionary:
prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }

# If you use the items() method, you can get (key,value) pairs:
print(prices.items())

# However, what if you wanted to get a list of (value, key) pairs instead? Hint: use zip().
pricelist = list(zip(prices.values(),prices.keys()))
print(pricelist)

#  this allows you to perform certain kinds of data processing on the dictionary data,
# such as min, max, sorted etc.
sorted_pricelist = sorted(pricelist)
print(sorted_pricelist)

# be aware that zip() stops once the shortest input sequence is exhausted.
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))
