from multiprocessing import Lock
from contextlib import contextmanager

# context managers - tool for resource management; allow you to allocate and release resources precisely

# example
with open("notes.txt", "w") as open_file:
    open_file.write("hello")

# example
lock = Lock()
with lock:
    print(2 * 2)




# custom context manager as a class
class ManagedFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    # This will be executed as soon as we enter the "with" statement
    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exp_type, exp_value, exp_traceback):
        if self.file:
            self.file.close()
        if exp_type is not None:
            print("exception handled")
        # print("exc:", exp_type, exp_value)
        print("exit")
        # To prevent exception from being raised
        return True

with ManagedFile("notes.txt") as file:
    print("do something")
    file.write("some example")
    file.something()
# what happens if exception occurs...
print("continuing")




# custom context manager as a function
@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        # yielding will temporarily suspend its own execution
        yield f
    finally:
        f.close()

with open_managed_file("notes.txt") as f:
    f.write("Hello")
    # when we exit the "with" statement, the function will continue running
