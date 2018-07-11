names = set()           # Doesn't repeat the elements
names.add("Michele")
names.add("Robin")
names.add("Michele")
print 'Set names:', names       # set(['Michele', 'Robin'])

value = list()      # declaring an empty list similar to value = []
value.append(3)
value.append(4)
value.append(3)     # This repeated 3 will not be discarded like in sets
value.append('John')
print 'List value =', value    # [3, 4, 3, 'John']
