print("String Concepts !")

# Declare strings
a = 'I am a single quoted string'
b = "I am a double quoted string"
c = """I am a tripple quoted string"""
print(a)        # I am a single quoted string
print(b)        # I am a double quoted string
print(c)        # I am a tripple quoted string
# This gives me the same result

# If I want to use quotes in a single inverted comman in a single quoted line then I should use escape character \
d = 'I am a single quoted string. Aren\'t I ?'
print(d)    # I am a single quoted string. Aren't I ?

h = "Hello"
p = " Python"
print(h + p)  # Hello Python
print("Lenth of string:"), len(h)  # gives the length of string which will be 5 in this case

x = "Hello "
y = 07  # which is a number
print(x + str(y))  # Hello 7   ...typecasting and concatenation of string

my_string = 'comma, seperation'
value1, value2 = my_string.split(',')                       # seperated the string by ','
comma_seperated_string = value1 + value2
print 'Comma Seperated String:', comma_seperated_string     # comma seperation
