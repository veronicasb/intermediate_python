import copy

org = 5
# this creates a new variable with the same reference (both variables point to the same number)
# the variables are still independent
cpy = org

# mutable types more require care
# this example shows that modifying a copy of a mutable type still affects the original
ls = [0, 1, 2, 3, 4]
ls_cpy = ls
ls_cpy[0] = -10
print(ls)
print(ls_cpy)

'''
shallow copy: 1 level deep, only references nested child objects
deep copy: full independent copy
'''

# shallow copies

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# or
cpy = org.copy()
# or
cpy = list(org)
# or
cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

# nested list - this will show that modifications to a shallow copy affect the original
org2 = [[0, 1, 3], [4, 5, 6]]
cpy2 = org2.copy()
cpy2[0][0] = -10
print(cpy2)
print(org2)



# deep copies - doesnt affect the original

org2 = [[0, 1, 3], [4, 5, 6]]
cpy2 = copy.deepcopy(org2)
cpy2[0][0] = -10
print(cpy2)
print(org2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Val', 21)
person1cpy = person1

# This will show that original gets affected
'''
person1cpy.age = 28
print(person1.age)
print(person1cpy.age)
'''

person1cpy = copy.copy(person1)
person1cpy.age = 28
print(person1.age)
print(person1cpy.age)


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Monica', 28)
p2 = Person('Joe', 36)

# This will show that original gets affected
'''
c1 = Company(p1, p2)
c1cpy = copy.copy(c1)

c1cpy.boss.age = 56
print(c1cpy.boss.age)
print(c1.boss.age)
'''

c1 = Company(p1, p2)
c1cpy = copy.deepcopy(c1)

c1cpy.boss.age = 56
print(c1cpy.boss.age)
print(c1.boss.age)