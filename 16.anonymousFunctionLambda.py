# Lambda forms can take any number of arguments but return just one
# Can not be directly called to print because lambda requires an expression
# Just Like inline function in C++


def sum(arg1, arg2): return arg1 + arg2  # Function definition is different


# all arguments should be used in the definition
# similar to: def sum(arg1, arg2): return arg1 + arg2
print 'Total 1 =', sum(5, 2)
print 'Total 2 =', sum(10, 23)
