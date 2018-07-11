# Tuples are sequence just like list
# But they can not be changed
# Uses paranthesis
# Iteration, concatenation, membership, length is possible like List

tup1 = ('Prasad', 1, 'Programs', 10, 'Python', 1993)
tup2 = (0, 1, 2, 3, 4, 5)               # Declaring a number tuple
tup3 = 'P', "R", "A", "S", "A", "D"  # Single inverted comma is also applicable
tup4 = (50,)                         # Tuple containing single value should have comma
normalVar = (80)
# But this is not a tuple it will be declared like normal variable

print 'Tuple 1 =', tup1
print 'Tuple 2 =', tup2
print 'Tuple 3 =', tup3
print 'Tuple 4 =', tup4
print 'Tuple 3 =', tup3
print 'Normal Variable =', normalVar

# Accessing values in tuple
print 'tup1[0] =', tup1[0]          # aceesing 1st element in tuple using indexing
print 'tup2[0:5] =', tup2[1:5]      # Slicing is similar to that of lists or strings

# Operation on Tuples
tup5 = tup1 + tup2      # We can not change the values of tupil we can append the existing one
print 'tup5 =', tup5    # ('Prasad', 1, 'Programs', 10, 'Python', 1993, 0, 1, 2, 3, 4, 5)
del tup1                # Deleting tuple
print tup1              # Trying to print deleted tuple which will produce error
