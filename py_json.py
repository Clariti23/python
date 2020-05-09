# JSON is commondly used with data APIs.
# Here is how we can parse JSON into a Python dictionary.

import json

# Sample JSON

userJSON = '{"first_name": "John", "last_name":"Doe", "age":30}'

# Parse to dict
user = json.loads(userJSON)

# print(user)  #=> {'first_name': 'John', 'last_name': 'Doe', 'age': 30}
# print(user['first_name'])  #=> John

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
