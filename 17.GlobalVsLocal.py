my_list = [1, 2, 3]
my_var = 5
global var2
var2 = 8

non_global_var = 7


def add_to_list(fun_list):
    fun_list.append(4)      # Making changes to the list by appending
    print 'In add_list function, fun_list =:', fun_list   # [1, 2, 3, 4]
    print 'In add_list function, my_list =:', my_list	  # [1, 2, 3, 4]


def change_var(var):
    print 'In change_var function, var =', var	 			# 5
    my_var = 10
    print 'In change_var function, my_var =', my_var		# 10


def change_var_globally(var):
    print 'In change_var_globally function, var =', var  			# 5
    global my_var  # global variable declaration in function works only
    my_var = 10
    print 'In change_var_globally function, my_var =', my_var		# 10


def check_global_var():
    # I am not declaring any variable, still it is detecting the my_var because it was made set global
    print 'Checking global variable in another function:', my_var   # 15 it works fine anywhere
    print 'Global variable declared outside of functions:', var2    # 8
    # var2 = 9   I am not able to 'change' the global var declared outside of function becuase it will be local for this definition

    print 'non_global variable declared outside of the function:', non_global_var


print 'Before add_to_list call, my_list =', my_list  		  # [1, 2, 3]
add_to_list(my_list)
print 'After calling add_to_list, my_list =', my_list		  # [1, 2, 3, 4]

print 'Before change_var call, my_var =', my_var              # 5
change_var(my_var)
print 'After calling change_var, my_var =', my_var		      # 5
# I get the same value though i change the variable value in function because it is not declared as global

# now try to change the variable value by making it global in function definition
change_var_globally(my_var)
print 'After calling change_var_globally, my_var =', my_var   # 10
# I get changed value for the variable after declaring that variable as global in defination

my_var = 15     # changing the global variable value declared in defination
check_global_var()

'''
Conclusion:
1. global variable declared in function will have read as well as write access all over the program
2. global variable declared outside the function definition will have read access all over the Programs but not able to write in any function
3. global variable declared outside the function will be similar to normal variable
4. normal variable can be used in the function (in fact it will work like global until any write operation. When you assign something to it, it becomes local)
'''
