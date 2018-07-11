def my_function():		# This is function definition and must be before calling the function
    print 'my_function has been called!'


def add(a, b):		# defining another function
    c = a + b
    return c


def mix_function(int_var, string_var, float_var=3.14):  # float_var is a default argument
    print 'In mix_function!'
    print 'int_var =', int_var		  # 15
    print 'string_var =', string_var  # prasad
    print 'float_var =', float_var	  # 3.14 if 3rd float type argument is not passsed


my_function()				# function call
result = add(5, 10)			# Calling the function and catching the returned value as wel
print 'Result of addition:', result

mix_function(15, 'prasad')
mix_function(15, 'prasad', 1.414)
