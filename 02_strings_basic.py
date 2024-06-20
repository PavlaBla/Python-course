symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

# Fix it so that the symbols variable holds the value 'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
symbols = symbols + ',GOOG'

print(symbols)

# Add 'HPQ' to the front the string:
symbols = 'HPQ,'+ symbols

print(symbols)

# Experiment with the in operator to check for substrings.
# At the interactive prompt, try these operations:

A = 'IBM' in symbols
B = 'AA' in symbols
C = 'CAT' in symbols

print(A,B,C)

D = symbols.find('MSFT') 

print(D)


