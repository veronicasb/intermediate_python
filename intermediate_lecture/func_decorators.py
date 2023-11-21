import functools

# function decorators - most common; a functon that takes another function as 
# an arguement to extend the abilities of another function without modifying it
def start_end_decorator(func):
    # a wrapper (an inner function)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

# functions in Python are first-class objects (like any object, they can be defined inside another function,
# passed as an argument to another function, or returned from other functions)
@start_end_decorator
def add5(x):
    return x + 5

# without "*args, **kwargs" we cant pass arguments to our functions
result = add5(10)

# None will be returned unless a return statement is included within the wrapper function
print(result)

# This will show that the identity our 'main' function gets confused with the wrapper function
# To fix this, use functools decorator over wrapper function 
print(help(add5))
print(add5.__name__)



def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}")

greet("Valorie")


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # will extract the name, arguments, and keyword arguments
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        # prints information of function
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        # prints information about return value
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

# nested decorators - will execute in the order their listed
# details before calling func() in debug decorator will execute, then details before func() in start_end_decorator will execute
@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello, {name}"
    print(greeting)
    return greeting

say_hello("Lexi")

# *args (all non-keyword arguments) - not a dictionary
# *kwargs (all keyword arguments) - a dictionary