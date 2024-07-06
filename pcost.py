import csv
import pprint

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, mode= 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
                 # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)
    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

# makes the script universal for different files 

cost = portfolio_cost(filename)
print('Total cost:', cost)