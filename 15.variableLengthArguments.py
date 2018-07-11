def my_function(formalArgument, *anyVariableType):  # *variable holds any variable arguments
    print 'Formal Argument Output is:', formalArgument
    print 'Now variable-length arguments:'
    for var in anyVariableType:  # This tuple remains empty if no additional arguments are passed
        print var
    print 'Any Variable Type output:', anyVariableType


my_function('hi')  # This was taken by formalArgument
print '--------First Function call has been completed!--------'

my_function(10.5, 'hello', 30, 3.14, 'prasad')  # 10.5 will be catched by formalAguments,
#'hello', 30, 3.14, 'prasad' will be caught by tuple-variable length arguments
