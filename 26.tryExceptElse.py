try:
    # If code in this try block doesn't work or executed completely;
    # It will run the except block
    # x = 0   If I uncomment this then error will not be there and therefore this try block will be executed completely
    print 'Just Before Error.'
    x = x + 2  # Making error by using variable before assignment
    print "This will not execute if error is present before this"
    x = 5
except:
    print "In Except Block. x = 8. Try didn't work!"  # This will execute only if try block doesn't work
    x = 2

else:
    # If try is correct and therefore except is not executed
    x = 23
    print 'In Else Block. x = 23. Runs only when there is no exception'

finally:
    # This will execute all the time irrespective of try, except, else
    print 'In Finally Block value of x =', x
