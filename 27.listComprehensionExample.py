# To find even numbers from 1 to 10

print "Program output without LC:"
for num in range(1, 11):     # the iterator
    if (num % 2) == 0:       # conditional filtering
        print num            # output-expression

print "Program output with LC:"
print [num for num in range(1, 11) if (num % 2) == 0]
