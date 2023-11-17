import sys, timeit

# tuples - ordered, immutable, allows duplicates
# can treat tuples like a list but it's immutable (nothing can be modified)
mytuple = tuple(["Max", 8, "Charlotte"])
print(mytuple)
# or
mytuple = ("Max", 8, "Charlotte")
print(mytuple)

for element in mytuple:
    print(element)

# tuples are best for list-like structures that have to stay the same (i.e. a list of vowels)
# indexing is exclusive
print(mytuple[::-1])

# Unpacking a tuple
tup = "Veronica", 25, "Charlotte"
name, age, city = tup
print(name)
print(age)
print(city)

# Tuples are more efficient - use less memory and are created much faster than lists
ls = [1, 2, 3]
tup1 = (1, 2, 3)
print(sys.getsizeof(ls), "bytes")
print(sys.getsizeof(tup1), "bytes")
print(timeit.timeit(stmt="[1, 2, 3]", number=1000000))
print(timeit.timeit(stmt="(1, 2, 3)", number=1000000))