# Dictionary - unordered, mutable (modifiable)
mydict = {"name": "Veronica", "age": 25, "city": "Charlotte"}
# or
mydict2 = dict(name="Veronica", age=25, city="New York")

# to remove a pair - del or .pop()
del mydict["name"]
print(mydict)
print(mydict2)
mydict2.pop("city")
print(mydict2)
# can use .popitem() to pop the last pair in the structure

if "name" in mydict:
    print(mydict["name"])

# return lists of the elements in a dictionary
print(mydict.keys())
print(mydict.values())
print(mydict.items())

# Best to use .copy() when copying data structures
mydict.update(mydict2)
print(mydict)

# Any immutable (non-modifiable) object can be set as a dictionary key
