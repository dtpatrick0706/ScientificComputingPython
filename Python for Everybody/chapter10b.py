## Comparing and Sorting Tuples ##
# Sorting a List of Tuples #

# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() methos and sorted() function

d = {'a': 10, 'b': 1, 'c': 22}
d.items()
# dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items())
# [('a', 10), ('b', 1), ('c', 22)]

#------------------------------------------------------------------------------------#

# Using sorted() #

# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence

d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
t
# [('a', 10), ('b': 1), ('c', 22)]
for k, v in sorted(d.items()):
    print(k, v)
# a 10
# b 1
# c 22

#------------------------------------------------------------------------------------#

# Sort by calues instead of Key #

# If we could construct a list of tuples of the form (value, key) we could sort by value
# We do this with a for loop that creates a list of tuples

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]

#------------------------------------------------------------------------------------#

