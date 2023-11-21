import sys
# generators - are functions that return an object that can be iterated over
# special because they generate elements in object "lazily" (generate items one at a time and only when you ask for it )
# memory efficient, good for large data sets

# yield keyword
def mygenerator():
    yield 1
    yield 2
    yield 3

gen1 = mygenerator()

'''
for element in gen1:
    print(element)
'''

'''
value = next(gen1)
print(value)


val2 = next(gen1)
print(val2)
'''

# print(sum(gen1))

# print(sorted(gen1))

'''
def countdown(start):
    print("Starting")
    while start > 0:
        yield start
        start -= 1

cd = countdown(3)

val = next(cd)
print(val)

print(next(cd))
'''

# big advantage of generators - they're memory efficient
def firstn(num):
    num_ls = []
    n = 0
    while n < num:
        num_ls.append(n)
        n += 1
    return num_ls

print(sum(firstn(10)))
print(sys.getsizeof(firstn(1000)))

def firstn_gen(num):
    n = 0
    while n < num:
        yield n
        n += 1

print(sum(firstn_gen(10)))
# dont have to save all the numbers with a generator
# code will show generator object remains the same size no matter what argument is passed
print(sys.getsizeof(firstn_gen(1000)))

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, b + a

fib = fibonacci(30)
for i in fib:
    print(i)

# generator expressions (like list comprehension except with parentheses)
mygen = (i for i in range(10) if i % 2 == 0)
'''
print(next(mygen))
print(next(mygen))
next(mygen)
for element in mygen:
    print(element)
'''

mylist = [i for i in range(10) if i % 2 == 0]

# even when you convert generator object to a list, it's still smaller
print(list(mygen))
print(sys.getsizeof(list(mygen)))

print(mylist)
print(sys.getsizeof(list(mylist)))
