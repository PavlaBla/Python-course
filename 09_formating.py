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
