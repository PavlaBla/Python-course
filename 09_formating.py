import csv
import pprint
# formating numbers using f strings:
value = 42863.1

# 4 decimal places:
print(f'{value:0.4f}')

# 2 decimal places, moved to the right:
print(f'{value:>16.2f}')

# 2 decimal places, moved to the left:
print(f'{value:<16.2f}')

# 2 decimal places, moved to the right, stars:
print(f'{value:*>16,.2f}')

# you can also format a string and save it to 
# a new valuable:
f = '%0.4f' % value

# modify the report.py to create a table with 
# names, shares, price and change columns.

# first, each row should be represented as a tupple:
# (using functions crated earlier)
def portfolio_cost(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
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

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
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

# create valuables 
portfolio = portfolio_cost('portfolio.csv')
prices = read_prices('prices.csv')

# create new function to determinate difference of prices:
def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
         current_price = prices.get(stock['name'], 0)
        #  The get method of the dictionary is used here. 
        #  It returns the value (current price) associated
        #  with the given key (stock['name']). If the key is not
        #  found, it returns a default value of 0.
        #  This ensures that the code does not break if a
        #  stock name in the portfolio does not have a corresponding 
        #  current price in the prices dictionary
         change = current_price - stock['price']
         summary = (stock['name'], stock ['shares'], current_price, change)
         rows.append(summary)
    return rows

report = make_report(portfolio,prices)

# get tupples:
for r in report:
     print(r)

# format the tupples:
for name, shares, price, change in report:
     print(f'{name:>10s}{shares:>10d}{price:>10.2f}{change:>10.2f}')

# add headers:
headers = ('Name', 'Shares', 'Price', 'Change')

# create table:
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

# modify the code so that the price includes the currency symbol ($)

print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for r in report:
    print('%10s %10d %10s %10.2f' % (r[0], r[1], f'${r[2]:.2f}', r[3]))
    #because theres now a symbol and numbers in the price column, it became a string instead of a float!
    