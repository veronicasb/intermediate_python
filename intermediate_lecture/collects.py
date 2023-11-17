from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaabbbccc"
# Counter converts some value into a dictionary
mycounter = Counter(a)
print(mycounter)

# .most_common will return a list of tuples of dictionary pairs
print(mycounter.most_common(1))

# .elements to get all elements in dictionary
print(list(mycounter.elements()))

# this will create a class with specified fields
Point = namedtuple("Point", "x, y")
pt = Point(1, 2)
print(pt)

# OrderedDict will create a dictionary with a set order (ordered)
# kind of irrelevant since Python3 maintains order of dictionaries now
example = OrderedDict()
example['z'] = 523
example['c'] = 7
example['d'] = 45
print(example)

# defaultdict - regular dictionary that will return a default value if calling a key that is out of index
# prevents key errors
ex_dict = defaultdict(int)
ex_dict["a"] = 1
ex_dict["b"] = 2
print(ex_dict)
print(ex_dict["c"])


# deque - double ended queue (can add or remove elements from both ends)
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(10)
print(d)

d.popleft()
print(d)

# will iterate over list specified and append each element to the front of the deque
d.extendleft([8, 7, 132])
print(d)

# will move elements to the right at specificed number of times
d.rotate(1)
print(d)
# will move elements to the left specified number of times
d.rotate(-2)
print(d)