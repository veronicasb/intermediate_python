# threading and multiprocessing allows us to run code in parallel to speed it up

'''
Process - an instance of a program (i.e. a Python interpreter, 1 firefox browser)

+ take advantage of multiple CPUs and cores (run code on multiple CPUs and cores in parallel)
+ seperate memory space (not shared except between processes)
+ great for CPU bound processing (i.e. doing expensive computations 
on large data sets - mulitprocessing allows us to process data on different CPUs to speed up code )
+ new processes are started independently from other processes
+ easily interruptible/killable
+ 1 GIL (Global Interpreter Lock) for each process --> avoids GIL limitations

- heavyweight (takes more memory)
- slower than starting a thread
- seperate memory space (memory sharing is not easy)
- IPC (inter-process communication) is more complicated

'''


'''
Threading - an entity within a process that can be scheduled ("lightweight process")
Processes can spawn multiple threads

+ threads within a process share the same memory
+ lightweight
+ starting is faster than starting a process
+ great for I/O-bound tasks (input-output tasks; i.e. program talking to slow devices - threading 
allows program to switch to other threads while waiting for communication to finish with other devices)

- limited by GIL; only 1 thread at a time (no parallel-ing)
- no effect for CPU-bound tasks
- not interruptible/killable (be wary of memory leaks)
- sharing memory --> sensitive race conditions (2 or more threads want to modify the same variable at the same time)

'''

'''
GIL (Global Interpreter Lock) - a mechanism in Python that allows only 1 thread to execute at a time

- needed in CPython for memory management, which is not thread-safe

Context:
- reference counting used for memory management: objects created in Python have a reference count variable,
that keeps track of number of references to object; when this count reaches 0, the memory used by object 
can be released
- problem with multithreading: reference count variable needs protection from race conditions where 2 threads
increase or decrease the value at the same time
------ if this happens, it can cause a memory leak that is never released, or incorrectly release memory that's still being referenced

To avoid GIL while parallel-computing:
- use multiprocessing
- use a free-threaded Python version (Jython, IronPython)
- use Python as a wrapper for third-party libraries ( i.e. NumPy and SciPy: wrappers in Python that call code that is executed in C)

'''

from multiprocessing import Process
from threading import Thread
import os
import time

# multiprocessing


# dummy example, not useful
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []

# a good number of processes should be the number of CPUs you have
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    # takes 2 arguments: target - callable object (function), args - arguments to pass to function if required 
    p = Process(target=square_numbers)
    processes.append(p)

# start each process
for p in processes:
    p.start()

# join processes - while waiting for process to finish, block main thread
for p in processes:
    p.join()

print("end main")


# Threading


threads = []

num_threads = 10

#create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start each thread
for t in threads:
    t.start()

# join threads
for t in threads:
    t.join()

print("end main")


# implementing threading and multiprocessing is very similar
