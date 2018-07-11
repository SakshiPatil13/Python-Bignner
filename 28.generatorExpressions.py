# To find even numbers from 1 to 10

LCResult = [num for num in range(1, 11) if (num % 2) == 0]
# List Comprehension uses square brackets and uses memory to store the results
print "Program output with LC:", LCResult

GEResult = ((num for num in range(1, 11) if (num % 2) == 0))
# Generator Expression uses parenthesis and do not use memory
print "Generator Expression Result:", GEResult  # returns object therefore do not use memory

# We can use it as expression to iterate
print "Accessing Generator Expression result:"
for obj in GEResult:  # Iterating through GE (Takes very less time though the range is too high)
    print obj
# Generator Expression is faster than List Comprehension
