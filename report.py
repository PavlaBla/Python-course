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
             try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
             except IndexError:
                  print('Empty row:', row)
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
            if len(row) < 3:
                print('Incomplete row:', row)
                continue
            try:
                dict = {'name':row[0], 
                        'shares' : int(row[1]), 
                        'price' : float(row[2])
                        }
                portfolio.append(dict)
            except ValueError as e:
                    print('Error processing row:', row, e)
    return portfolio

portfolio = portfolio_cost('portfolio.csv')
print(portfolio)

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    try:
        total_cost += s['shares'] * s['price']
    except KeyError:
        print(f"Price for {s['name']} not found in prices list")

print(total_cost)

# To clean up the output for debugging, consider using the pprint function.
pprint(portfolio)

# Write a function read_prices(filename) that reads a set of prices 
# into a dictionary where the keys of the dictionary are the stock 
# names and the values in the dictionary are the stock prices.

def read_prices(filename):
     
    prices = {}
    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
             try:
                  prices[row[0]] = float(row[1])
             except IndexError:
                 pass
    return prices

print(read_prices('prices.csv'))

prices = read_prices('prices.csv')
print(prices['IBM'])

# Tie all of this work together by adding a few additional statements to 
# your report.py program that computes gain/loss. These statements should
# take the list of stocks and the dictionary of prices and compute the 
# current value of the portfolio along with the gain/loss.

# Compute the current value of the portfolio
total_value = 0.0

for s in portfolio:
    try:
        total_value += s['shares']*prices[s['name']]
    except KeyError:
        print(f"Price for {s['name']} not found in prices list")

print (f'Current value: {total_value}')
print (f'Gain: {total_value - total_cost}')