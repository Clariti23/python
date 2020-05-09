#Strings in python are surrounded by single or double quotations.

name = 'Grant'
age = 27

# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Concatenate by position
# print('line 11')
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-String (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize a string
# print(s.capitalize())

# #Make all uppercase
# print(s.upper())

# # make all lower
# print(s.lower())

# #swap case
# print(s.swapcase())

#get length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'l'
print(s.count(sub))

# Starts with - returns a bool
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split a string into a list
print(s.split())

# Find position
print(s.find('r'))

#is all alphanumeric
print(s.isalnum())

#is all alphabetic
print(s.isalpha())

#is all numeric
print(s.isnumeric())
