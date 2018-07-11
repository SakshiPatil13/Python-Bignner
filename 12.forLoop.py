for any_var in range(0, 10):
    print 'any_var in for loop:', any_var  # o/p = 0123456789
# ---------------------------------------------------------

for any_var in range(0, 10, 1):
    print 'any_var in for loop with step 1:', any_var  # o/p = 0123456789
 # ---------------------------------------------------------

for any_var in range(0, 10, 2):
    print 'any_var in for loop with step 2:', any_var		# o/p = 0, 2, 4, 6, 8
 # ---------------------------------------------------------

for any_var in range(0, 10, -1):		# This for loop doesnot execute
    print 'any_var in for loop (0 to 10) with step -1:', any_var  # No output
 # ---------------------------------------------------------

for any_var in range(10, 0, - 1):		# 10 9 8 7 6 5 4 3 2 1
    print 'any_var in for loop (10 to 0) with step -1:', any_var  # print 1 less than the last limit
# ---------------------------------------------------------

for _ in range(0, 10):      # If I do not care about the variable
    print 'any task which we want to repeat for 10 times'     # This message will get printed 10 times
# ---------------------------------------------------------
