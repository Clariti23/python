def sayHello(name='Sam Smith'):
    print(f'Hello {name}')


# sayHello('Jill Mills') => 'Hello Jill Mills'
# sayHello() => with default 'Hello Sam Smith'

# Return values
# def getSum(num1, num2):
# total = num1 + num2

# return total

# Two ways to call the function
# print(getSum(3, 4))

# num = getSum(4, 5)
# print(num)

# A lamda function is a small anon function

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))  #=> outputs 13

# A lamda function can take any number of arguments,
# but can only have one expression like a JS arrow function