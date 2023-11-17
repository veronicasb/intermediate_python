import sys

# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

myset2 = set([1, 2, 3, 4])
print(myset2)

# Sets maintain no order
myset3 = set("hello")
print(myset3)

# This is an empty set
empty_set = set()

# This is an empty dictionary
empty_dict = {}
empty_dict2 = dict()

empty_set.add(1)
empty_set.add(2)
empty_set.add(23)
empty_set.add(54)
empty_set.add(12)
empty_set.add(0)

print(empty_set)

# .remove and .discard do the same things except .discard wont return an error if element isnt found
empty_set.remove(2)
empty_set.discard(1)

print(empty_set)

# .pop will remove a random element since sets are unordered
print(empty_set.pop())
print(empty_set)

# .clear to empty set completely
# empty_set.clear()
# print(empty_set)

for element in empty_set:
    print(element)


odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

# combine sets without duplication
u = odds.union(evens)
print(u)
# .update CAN do the same thing as union, except it will modify set in place
# and you can set this value to a variable (will return none)
odds.update(evens)
print(odds)

# return elements that are only found in BOTH elements
i = evens.intersection(primes)

seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}

# return elements from set a that dont exist in set b
diff1 = seta.difference(setb)
print(diff1)

# return elements from set b that dont exist in set a
diff2 = setb.difference(seta)
print(diff2)

#return all elements that are different
diff3 = seta.symmetric_difference(setb)
print(diff3)

# below code will do everything shown above, except set will be modified in place
# seta.intersection_update(setb)
# seta.difference_update(setb)
# seta.symmetric_difference_update(setb)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
set3 = {7, 8}
# subset = ALL elements of first set are also in second set
print(set2.issubset(set1))
print(set1.issubset(set2))

# superset = ALL elements of second set are within first set
print(set1.issuperset(set2))
print(set2.issuperset(set1))

# disjoint = 2 sets that have no elements in common
print(set1.isdisjoint(set3))

# JUST DONT SET A VARIABLE EQUAL TO ANOTHER VARIABLE BECAUSE ITS POINT TO THE SAME SHIT IN MEMEORY
# JUST USE .COPY() OR DATATYPE METHOD ALWAYS 

# a frozen set is the immutable (non-modifiable) version of a set
a = frozenset([1, 2, 3, 4, 5])
print(a)
b = set([1, 2, 3, 4, 5])

print(sys.getsizeof(a), "bytes")
print(sys.getsizeof(b), "bytes")