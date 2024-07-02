# dictionaries:
# You can look up a value that might not exist and 
# provide a default value in case it doesn't.
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}

# name = d.get(key, default)

price = prices.get('IBM', 0.0)
price2 = prices.get('SCOX', 0.0)

print(price, price2)

# Sets are collection of unordered unique items.
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])

# Sets are also useful for duplicate elimination.
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique = set(names)
print(unique)

# Additional set operations:
# add an item
unique.add('CAT')

# remove an item
unique.remove('YHOO')

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

# set union {'a', 'b', 'c', 'd'}
s1 | s2

# set intersection {'c'}
s1 & s2

# set difference {'a', 'b'}
s1 - s2