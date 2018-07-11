
names = []  # enpty list
print 'names empty list:', names  # printing my list    []

names = ["mark", "tom", "john"]
print 'names list with elements:', names    # ['mark', 'tom', 'john']
print 'names[1]:', names[1]     # tom
print 'names[-2]:', names[-2]   # tom

names.append("tony")        # this will append the name name tony to the existing list
print 'after appending/adding element to the list:', names  # ['mark', 'tom', 'john', 'tony']

age = [50, 20, 18, 21]  # creating a new list
names.extend(age)       # adding the newly created list to the existing names list
print 'after extending the list:', names    # ['mark', 'tom', 'john', 'tony', 50, 20, 18, 21]

names.remove("tom")  # to remove any value here it is'tom'
print 'removing \'tom\' from the list:', names  # ['mark', 'john', 'tony', 50, 20, 18, 21]

print 'Now length of list-name:', len(names)    # 7
print 'Max value in list age:', max(age)        # 50
