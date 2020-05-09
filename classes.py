# a Class is like a blueprint for creating an object. An object


# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


#Extend class


class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
grant = User('Grant Ferowich', 'grant@gmail.com', 27)

# Init customer object
jill = Customer('Jill', 'jill@gmail.com', 25)

jill.set_balance(500)

print(jill.greeting())
# grant.has_birthday()
# print(grant.greeting())
