from functools import reduce

# lambda arguments: expression
# basically creates a simple function that takes an argument in one line of code
#
# best used if you need to use a simple function once
# best used for higher order functions that take other functions as arguments
add10 = lambda x: x + 10
print(add10(4))


# or
def add10(x):
    return x + 10


print(add10(5))


# lambda's can also take more than 1 argument
mult = lambda x, y: x * y
print(mult(2, 3))


# lambda is typically used along with built-in functions like sorted, map, filter, and reduce
# sorted
points2d = [(1, 3), (7, 2), (3, 9)]
points2d_sorted = sorted(points2d)
print(points2d)
print(points2d_sorted)

# this code will sort list based on y coordinate instead of x
points2d_sorted = sorted(points2d, key=lambda x: x[1])
print(points2d_sorted)

# This code does the same thing as above
def sort_by_y(x):
    return x[1]
points2d_sorted = sorted(points2d, key=sort_by_y)
print(points2d_sorted)

# This code sorts the tuples according to the sum of the x, y coordinates
points2d_sum_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d_sorted)


# map - iterates over a sequence and performs some operation over each element
# map(func, seq)
a = [2, 65, 132, 98]
b = map(lambda x: x * 2, a)
print(list(b))
# or
c = [x * 2 for x in a]
print(c)


# filter - returns all elements that return True when evaluated by function argument
# filter(func, seq) - function must return a Boolean

# this code will return a list of elements from the argument that are even numbers
d = filter(lambda x: x % 2 == 0, a)
print(list(d))
# or
d = [x for x in a if x % 2 == 0]
print(d)


# reduce - repeated applies function to elements, then returns a single value
# reduce(func, seq)

# this code did something resembling what the accumulate function does (from the last lecture)
e = reduce(lambda x, y: x * y, a)
print(e)