import csv
from pprint import pprint
# in previous exercises I've created a code
# which read a document and provided a simple calcs:

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
    return total_cost

# Using this code as a rough guide, create a new 
# file report.py. In that file, define a function 
# read_portfolio(filename) that opens a given portfolio 
# file and reads it into a list of tuples. 

# make a variable that’s initially set to an empty list
def portfolio_cost(filename):
     
    portfolio = []

# turn each row into a tuple and append it to the list
    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
             holding = (row[0], int(row[1]), float(row[2]))
             portfolio.append(holding)
    return portfolio

print(portfolio_cost('portfolio.csv'))

# now modify the function to represent each stock in the portfolio with a dictionary 
# instead of a tuple. In this dictionary use the field names of "name", 
# "shares", and "price" to represent the different columns in the input file.

def portfolio_cost(filename):
     
    portfolio = []
    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
             dict = {'name':row[0], 
                     'shares' : int(row[1]), 
                     'price' : float(row[2])
             }
             portfolio.append(dict)
    return portfolio

portfolio = portfolio_cost('portfolio.csv')
print(portfolio)

total = 0.0
for s in portfolio:
     total += s['shares'] * s['price']

print(total)

# To clean up the output for debugging, consider using the pprint function.
pprint(portfolio)