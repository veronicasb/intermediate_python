import random, secrets
import numpy as np

# generate psuedo-random numbers (seems random but not actually)
# NOT RECOMMENDED FOR SECURITY PURPOSES

# for a random float in range from 0 to 1
a = random.random()
print(a)

# for a random float in some range
b = random.uniform(1, 10)
print(b)

# for a random integer in some range (inclusive)
c = random.randint(1, 100)
print(c)

# for a random integer in some range (exclusive)
d = random.randrange(1, 100)
print(d)

# for a random value from a normal distribution with a mean of some number and a standard deviation of another number
# useful for statistics
e = random.normalvariate(0, 1)
print(e)

ls = list("aerhaghl")
# for a random value from a list
z = random.choice(ls)
print(z)
# for a series of random values from a list with no duplicates
x = random.sample(ls, 3)
print(x)
# for a series of random values from a list with duplicates
y = random.choices(ls, k=5)
print(y)
# to shuffle a list
random.shuffle(ls)
print(ls)

# to reproduce "random" values
random.seed(35)
print(random.random())



# FOR SECURITY-SENSITIVE RANDOM VALUES

# for a random int below a specified upper-bound (exclusive)
a = secrets.randbelow(35)
print(a)

# for a random int of specified bits
b = secrets.randbits(4)
print(b)

# for a random selection from a list
ls2 = list("ryjwarth") 
z = secrets.choice(ls2)
print(z)


# random numpy values/arrays/matrices


# for a random array of floats of specified matrix size
a = np.random.rand(3, 4)
print(a)

# for a random array of a range of ints of a specified matrix size
b = np.random.randint(0, 10, (3, 4))
print(b)

# will only shuffle elements along axes
arr = np.array([[231, 56, 1], [23, 78, 978], [34, 67, 34]])
np.random.shuffle(arr)
print(arr)

# CAUTION: numpy random generator is different from random module library
np.random.seed(1)
print(np.random.rand(3, 3))
