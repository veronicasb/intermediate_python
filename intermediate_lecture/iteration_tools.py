# collection of tools for handling iterators
# iterators are data types that can be used in a for loop

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
a = [3, 21, 87, 2]
b = [7, 12, 67, 978]


# product - results in a list of tuples of every combination of elements
# will return an itertools object
prod = product(a,b)
print(list(prod))


# permutations - results in all possible orders of some imput of a specified length
c = [423, 7, 4, 54]
perm = permutations(c)
perm2 = permutations(c, 2)
print(list(perm2))
print(list(perm))


# combinations - make all possible combinations of a specified length
d = [132, 54, 45]
comb = combinations(d, 2)
# this will return combintations without any duplicate pairs, even if the order is different
print(list(comb))
# this will return literally all possible combinations, even elements flipped
print(list(permutations(d, 2)))

# this will return combinations along with same-element pairs
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))


# accumulate - adds each element one at a time
z = [2, 23, 8, 1]
acc = accumulate(z)
# does what accumulate does expect using multiplication
acc2 = accumulate(z, func=operator.mul)
print(z)
print(list(acc))
print(list(acc2))
# accumulate basically iterates thru each element, then does some kind of operation or comparison to the element that came before it

def smaller_than(num):
    return num < 150

# groupby - returns a dictionary; groups values according to some condition
e = [132, 6, 234, 7]
group = groupby(e, key=smaller_than)
for key, value in group:
    print(key, list(value))

# this does the same thing as above, except more concisely through the use of lambda function
group2 = groupby(e, key=lambda x: x<150)
for key, value in group2:
    print(key, list(value))

# kind of like groupby function in SQL
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28} ]
group3 = groupby(persons, key=lambda x: x['age'])
for key, value in group3:
    print(key, list(value))

# count - takes a start value, then iterates infinitely
for i in count(10):
    if i > 20:
        break
    print(i)
    
# cycle - cycles infinitely thru iterable
z = [53, 7, 21]
for element in cycle(z):
   print(element)

# repeat - repeats specified object infinitely, or for specified number of times
# code below will repeat 1 two times
for element in repeat(1, 2):
    print(element)