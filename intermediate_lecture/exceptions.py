# Errors vs exceptions

# Handling exceptions
x = -5
# if x < 0:
#    raise Exception('x should be positive')
# or
# assert (x >= 0), "x is not positive"
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e, ": Cant divide by 0")
except TypeError as e:
    print(e)
else:
    print("Everything works")
finally:
    print("Ok")


# Defining exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high!")
    elif x < 5:
        raise ValueTooLowError("Value is too low", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message + ":", e.value)