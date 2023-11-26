# Arguments vs. Parameters

# This function takes a "Parameter"
def print_name(name):
    print(name)

# This calls a function and passes an "Argument"
print("Veronica")




# Positional and keyword arguments

def foo(a, b, c):
    print(a, b, c)

# This calls a function and passes "positional" arguments
foo(1, 2, 3)

# This calls a function and passes "keyword" arguments - in this case, the order of arguments doesnt matter
foo(a=1, b=2, c=3)

# You can combine both usages, but you can call a positional argument after a keyword argument
foo(1, c=3, b=2)




# Default arguments
# must be at the end of function parameters
def greet(name="stranger"):
    print("Hello", name)

print(greet())




# Variable-length arguments (*args and *kwargs)

def far(a, b, *args, **kwargs):
    # an asterisk * means you can pass any number of positional arguments
    # 2 asterisks means you can pass any number of keyword arguments
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

# *args and *kwargs are optional arguments
far(1, 2, 3, 4, 5, six=6, seven=7)




# Container unpacking into function arguments

def foo(a, b, c):
    print(a, b, c)

# the length of the container MUST match the number of parameters
ls = [0, 1, 2]
print(foo(*ls))
# the lenth of container MUST match number of parameters and keys but match parameters
dictionary = {'a': 1, 'b': 2, 'c': 3}
print(foo(**dictionary))




# Local vs. global arguments

def square():
    # to access a global variable anywhere, you must use "global" keyword
    global number
    x = number
    number = 3
    print("Number inside function: ", x)

number = 0
square()
print(number)




# Parmeter passing (by value or by reference)
# Call by object/call by object reference
'''
Parameters/Arguments passed in are references to an object, but the reference is passed by value.

Mutable objects CAN be changed within a function, but if you reassign the
reference within a function, then the outer reference will still point to its original value (global vs local variables).
Immutable objects CANT be changed in a function, but immutable objects contained within
a mutable container can be REASSIGNED within a function.
'''

def bar(x, ls=[]):
    x = 5
    # if I add this line, mylist wont change how we saw before because we've now created a local variable
    ls = [200, 300, 400]
    ls.append(3)

# does not change var
var = 10
bar(var)
print(var)

# changes mylist
mylist = [1, 2, 3]
bar(var, mylist)
print(mylist)

'''
To reiterate: mutable objects CAN be changed within a function, but if you reassign the reference within the function,
it creates a NEW LOCAL VARIABLE
'''
