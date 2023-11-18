# JSON - javascript object notation
# lightweight data format for data exchange
# used commonly in web applications

import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "Phoenix", "hasChildren": False, "title": ["engineer", "CEO"]}

# converting a Python dictionary to a JSON file is called serialization or encoding
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("person.json", "w") as open_file:
    json.dump(person, open_file, indent=4)


# deserialization/decoding - converting json back to python object
person2 = json.loads(personJSON)
print(person)

with open("person.json", "r") as file:
    person3 = json.load(file)
    print(person)



# One way of encoding/serializing a custom object
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Veronica", 25)

# custom encoding function
def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object not JSON serializable")
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# Another way of encoding/serializing customer object
# dont forget to import module JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj) 
    
userJSON2 = json.dumps(user, cls=UserEncoder)
print(userJSON2)
print(type(userJSON2))
# or
userJSON3 = UserEncoder().encode(user)
print(userJSON3)

# Decode a custom object

# this will decode json objects into dictionaries but if we want to decode them back into class objects...
user1 = json.loads(userJSON)
print(user1)
print(type(user1))
user2 = json.loads(userJSON2)
print(user2)
user3 = json.loads(userJSON3)
print(user3)

# ...do this
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user4 = json.loads(userJSON, object_hook=decode_user)
print(type(user4))
print(user4.name)