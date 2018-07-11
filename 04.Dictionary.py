dictVariable = {'Name': 'Prasad', 'Age': 23, 'Class': 'First'}  # declaring a dictionary
# 'Name','Age','Class' are called keys of dictionary which holds the value

# Accessing values of dictionary using key
print "dictVariable['Name'] =", dictVariable['Name']  # Prasad
print "dictVariable['Age'] =", dictVariable['Age']    # 23

# if we try to access the data which is not in the dictionary it will produce error
# e.g if we write print dictVariable['Education']
# because Education key is not present in the dictionary

print "Length of Dictionary =", len(dictVariable)   # 3

# Returns a list of dictionary's (key,value) tuple pairs
print 'List of Dictionary Items =', dictVariable.items()
# [('Age', 23), ('Name', 'Prasad'), ('Class', 'First')]

print 'Keys of Dictionary =', dictVariable.keys()       # ['Age', 'Name', 'Class']

print 'Values of Dictionary =', dictVariable.values()   # [23, 'Prasad', 'First']

# Updating Dictionary
dictVariable['Age'] = 24
print 'My Dictionary =', dictVariable   # [23, 'Prasad', 'First']

dictVariable['Degree'] = 'B.Tech'   # Adding new key-value
print dictVariable
# {'Age': 24, 'Name': 'Prasad', 'Degree': 'B.Tech', 'Class': 'First'}

del dictVariable['Degree']  # Deleting dictionary elements
print 'After deleting key Degree =', dictVariable
# {'Age': 24, 'Name': 'Prasad', 'Class': 'First'}

dictVariable.clear()  # Remove all the entries but do not delete it
print 'cleared Dictionary =', dictVariable   # {}

del dictVariable    # Delete entire dictionary
print dictVariable  # Shows error because we have deleted it
