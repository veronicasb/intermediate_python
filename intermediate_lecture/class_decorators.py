
# Class decorators - do the same as function decorators but they maintain and update state

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # allows to execute object of this class
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()

'''
typical use cases - a timer decorator, a debug decorator to print more info about
the called function, a check decorator to check if arguments fulfill some requirements,
register funtion (plugins), cache return values, or add information or update state
'''