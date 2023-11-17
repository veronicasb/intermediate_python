# strings are the most used data types in python
# ordered, immutable
mystring = "hello world"
backwards = mystring[::-1]
print(backwards)

for letter in mystring:
    print(letter)

if "i" in mystring:
    print("yes!")
else:
    print("no!")

# IMMUTABLE MEANS THAT IT CANT BE MODIFIED IN PLACE

# -1 means it doesnt exist in the string, otherwise method will return index
print(mystring.find("p"))

# nothing changes if word to replace isnt found
print(mystring.replace("Worrld", "Universe"))

newstring = "How are you?"
# .split() converts string into list by whatever character specified
# character specified will be removed
ls = newstring.split()
print(ls)

# .join will combine the elements of a list with whatever character is specified
# less expensive (in terms of memory and time) than a for loop
print(" ".join(ls))
print("a".join(ls))

# formatting strings (% or .format() or f-Strings)

# old formatting style
example = "escape"
test_string = "the example word is %s" % example
print(test_string)

example2 = 4
test_string2 = "the example number is %d" % example2
print(test_string2)

example3 = 3.14
# specify digits or default for float is 6-7 digits
test_string3 = "the example float is %.2f" % example3
print(test_string3)

# new formatting style
test_string4 = "the example float is {:.3f}".format(example3)
print(test_string4)

test_string5 = "the example word and number is {} and {}".format(example, example2)
print(test_string5)

# NEWEST formatting style
# THIS RIGHT HERE EATS, FORGET THOSE OTHER STYLES - THEYRE ANNOOYYYIINNGGGG
test_string6 = f"the example word and number is {example} and {example2}"
print(test_string6)