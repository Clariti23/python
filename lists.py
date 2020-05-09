#a list is an ordered, changeable collection that allows duplicate members.

# Create a list (zero-indexed)
nums = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# Use a constructor

# nums2 = list((1, 2, 3, 4, 5))

# print(nums, nums2)

# Get a value
print(fruits[2])

# Get length of a list
print(len(fruits))

# Append element to list
fruits.append('pineapples')

# Remove from list
fruits.remove("apples")

# Insert into position
fruits.insert(2, 'banana')

# Remove with pop
fruits.pop(2)

# Reverse a list
fruits.reverse()

#Sort a list
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

print(fruits)