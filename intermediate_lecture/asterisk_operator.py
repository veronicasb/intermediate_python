# different uses of the asterisk
result = 5 * 7
print(result)

result = 2 ** 4
print(result)

zeros = [0] * 10
print(zeros)

str_example = "ab" * 3
print(str_example)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

# everything after the asterisk will be keyword-only parameters
def bar(d, e, *, f, g):
    print(d, e, f, g)

bar(1, 2, f=3, g=4)

def unpack(a, b, c):
    print(a, b, c)

# when unpacking arguments, the number of elements and/or keys must match parameters
myls = [1, 2, 3]
unpack(*myls)
mydict = {'a': 1, 'b': 2, 'c': 3}
unpack(**mydict)

