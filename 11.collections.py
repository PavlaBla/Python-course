from collections import Counter
from collections import defaultdict
from collections import deque

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# here are two IBM entries and two GOOG entries in this list.
# The shares need to be combined together somehow.

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares['IBM'])

# Problem: You want to map a key to multiple values.


holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print(holdings['IBM'])

# Problem: We want a history of the last N things. Solution: Use a deque.
history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
        ...