# On lists, slices can be reassigned and deleted.
# reassignment:
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12,13]

# deletion:
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]
print(a)

# break statement: to exit the loop and move on to other statement:
namelist = []
for name in namelist:
    if name == 'Jake':
        break

# continue statement: to skip one element and move on to the next:
lines = []
for line in lines:
    if line == '\n':    # Skip blank lines
        continue

# looping over inteegers:
# The syntax is range([start,] end [,step]). start and step are optional, default is 0 and 1
for k in range(10, 50, 2):
    print(k)

# enumerate function - adds an extra counter value to iteration.
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    print(i,name)

# You can iterate with multiple iteration variables. Each tuple is 
# unpacked into a set of iteration variables. The number of variables 
# must match the number of items in each tuple.
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    print(x,y)

# Zip function takes multiple sequences and makes an iterator that combines them.
# A common use of zip is to create key/value pairs for constructing dictionaries.
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)

# to get the values, you have to iterate
for column, value in pairs:
    print(column, value)

# basic counting examples:
for n in range (10):
    print(n, end=' ') # prints on one line

for n in range (10, 0, -1):
    print(n, end= ' ')