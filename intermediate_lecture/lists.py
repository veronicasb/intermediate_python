# lists - ordered, mutable, allow duplicates
my_list = ["banana", "cherry", "apple"]
print(my_list)

another_list = list()
print(another_list)

print(my_list[1])

for element in my_list:
    print(element)

for i in range(len(my_list)):
    print(my_list[i])

if "blueberry" in my_list:
    print(True)
else:
    print(False)

print(len(my_list))

# Append tacks element onto the end of a list
my_list.append("lemon")

# Insert tacks an element into a specified index
my_list.insert(1, "blueberry")

print(my_list)

my_list.remove("cherry")

# .sort() changes list in place while sorted() creates a new list
my_list.sort()
print(my_list)
print(sorted(my_list))

new_list = ["bag"] * 5
print(new_list + my_list)

# List slicing
a = new_list[1:5]
print(a)

# Step index - take list slice, then index it by step specified (default = 1)
b = new_list[1::2]
print(b)

# Assigning 2 lists equal to each other will point to the same place in memory
a = b
a = b.copy()
a = b[:]

# List comprehension - create a new list from existing list in 1 line
a = [1, 1, 2, 3, 4, 5, 6]
b = [i*i for i in a]

print(a.count(1))