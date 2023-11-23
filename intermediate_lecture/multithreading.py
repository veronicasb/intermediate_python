# more details about threading module

from threading import Thread, Lock, current_thread
import os
import time
from queue import Queue

'''
# recap

def square_numbers():
    for i in range(100):
        i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()

    # join threads (wait and block main thread until thread is complete)
    for thread in threads:
        thread.join()

    print("end main")

'''

# share data between threads
# threads have access to same memory space, so they have access to the same data (easy data sharing)
# use locks to prevent race conditions


'''

# define global variable
database_value = 0

def increase(lock):
    global database_value

    # lock prevents another thread from accessing some code at the same time
    # only one thread at a time can access code "within" the lock unitl release
    # you can use "with lock:" so you dont forget to release (kind of like opening files)
    lock.acquire()
    local_copy = database_value

    # processing
    local_copy += 1

    # In the first example, sleep time allows our program time to switch to the other thread
    # This is to show how "smart" threading is 
    
    time.sleep(0.1)

    database_value = local_copy
    lock.release()

if __name__ == "__main__":

    lock = Lock()
    print("start value:", database_value)

    # args should always be a tuple, even with 1 argument
    thread1 = Thread(target=increase, args=(lock, ))
    thread2 = Thread(target=increase, args=(lock, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value:", database_value)

    print("end main")

    # this code will yield an end value of 1 due to race conditions
    # (if you remove the time.sleep() bit, it will be 2 because you dont give the computer time to switch to the other thread)
    # but you should use Lock()

'''
# a daemon process and how to use queues for thread-safe data exchanges

# queue - linear data structure that uses the FIFO (first in, first out) order

def worker(q, lock):
    while True:
        val = q.get()
        # processing
        with lock:
            print(f'in {current_thread().name} got {val}')
            # in a threading environment, anytime you "get" a queue object, then process it, you must always use:
            # q.task_done()
        q.task_done()
        

if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        '''
        a daemon thread - when thread enters the infinite loop, it stocks immediately because 
        no items are added to the queue until AFTER this block of code. A daemon thread is a backgroud 
        thread that dies after the main thread dies.
        '''
        thread.daemon=True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    # this blocks main thread until all items in queue have been gotten and processed
    # q.join()
    q.join()

    # check if queue is empty:
    # q.empty()
    
    # A daemon thread will die at this point, so the worker() method will no longer be invoked
    # The daemon thread guaranteed breaking out of the infinite loop after processing in worker()
    print("end main")