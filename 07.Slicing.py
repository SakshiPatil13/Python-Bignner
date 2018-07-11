myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print 'myList:', myList
print 'myList[2] =', myList[2]
print 'myList[4:8] =', myList[4:8]          # to print the list from 4 to 7 in actual
print 'myList[5:9] =', myList[5:9]          # 5 and 9 are the indices
print 'myList[5:2] =', myList[5:2]          # we will get an empty list
print 'myList[5:-2] =', myList[5:-2]        # see, end_index-1 will be the limit i.e. -2-1 = -3
print 'myList[:] =', myList[:]              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'myList[2:] =', myList[2:]            # [2, 3, 4, 5, 6, 7, 8, 9]
print 'myList[:5] =', myList[:5]            # [0, 1, 2, 3, 4]
print 'myList[2:8:1] =', myList[2:8:1]      # [2, 3, 4, 5, 6, 7] Increments the index by step_size=1
print 'myList[2:8:2] =', myList[2:8:2]      # [2, 4, 6]
print 'myList[2:8:-1] =', myList[2:8:-1]    # [] reverse operation is not possible
print 'myList[8:2:-1] =', myList[8:2:-1]
# [8, 7, 6, 5, 4, 3]  Note the end is 1 less than end_index
# -------------------------------------------------------------------------------------------------------

myString = '0123456789'

print 'myString =', myString                    # 0123456789
print 'myString[2] =', myString[2]              # 2
print 'myString[4:8] =', myString[4:8]          # 4567
print 'myString[5:9] =', myString[5:9]          # 5678
print 'myString[5:2] =', myString[5:2]
# we will get an empty string (nothing) because step_size is by defualt 1 and in fwd direction
print 'myString[5:-2] =', myString[5:-2]
# 567 see, end_index-1 will be the limit i.e. -2-1 = -3
print 'myString[:] =', myString[:]              # 0123456789
print 'myString[2:] =', myString[2:]            # 23456789
print 'myString[:5] =', myString[:5]            # 01234
print 'myString[2:8:1] =', myString[2:8:1]      # 234567 Increments the index by step_size=1
print 'myString[2:8:2] =', myString[2:8:2]      # 246
print 'myString[2:8:-1] =', myString[2:8:-1]    # blank reverse operation is not possible
print 'myString[8:2:-1] =', myString[8:2:-1]
# 876543  Note the end is 1 less than end_index
