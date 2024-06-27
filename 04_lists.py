names = ["Elwood", "Jake", "Curtis"]
names.insert(2, "Aretha")
# adds new item to the list at given position
# vs .append adds item to the end of the list
print(names)

names[1] = "Joliet Jake"
# changes second item
print(names)

curtis = names.index("Curtis")
# finds positon of an item. if not found -> value error
print(curtis)

# removing item using the value. remove will remove only first occurence of an item
names.remove("Curtis")

# removin item using the index
del names[1]

s = [5, 79, 61, 3, 6, 5]
t = sorted(s)
print(t)
# creates new sorted list

names.count("Curtis")
# how many times does the item occure

# in general lists can't be edited, you allways create a new list.