from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time


# creating and starting multiple processes (recap)
'''
def square_numbers():
    for i in range(1000):
        i * i

if __name__ == "__main__":
    processes = []
    # good practice: number of processes should match number of CPUs on machine
    num_processes = os.cpu_count()

    # create processes and assign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all process
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block main program until all processes are finished
    for process in processes:
        process.join()
'''


# sharing data between processes
# using locks to prevent race conditions
# threading: share data using a global variable
'''
processes: since processes dont exist in the same memory space, they dont have access 
to the same public data, so they need special memory objects --> a Value (for a single value) 
or an Array (for multiple values)
'''
'''
def add_100(nums, lock):
    for i in range(100):
        time.sleep(0.01)
        # best to use lock with a context manager
        # cant use a regular for-loop in this case because index will create a local variable
        with lock:
            for i in range(len(nums)):
                nums[i] += 1

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("Array at begining is", shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Array at end", shared_array[:])

'''

# using queues (must be from multiprocessing module; for process-safe data exchanges)
'''
def square(nums, q):
    for i in nums:
        q.put(i * i)

def make_negative(nums, q):
    for i in nums:
        q.put(-1 * i)

if __name__ == "__main__":
    q = Queue()
    nums = range(1, 6)

    p1 = Process(target=square, args=(nums, q))
    p2 = Process(target=make_negative, args=(nums, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

'''

# using process pool to manage multiple processes

def cube(num):
    return num**3

if __name__ == "__main__":

    pool = Pool()
    nums = range(10)

    # map, apply, join, close

    # map - automatically allocates max number of available processes
    # splits iterable into equal-sized chunks
    result = pool.map(cube, nums)

    # this executes process using one element at a time
    pool.apply(cube, nums[0])
    
    pool.close()
    pool.join()

    print(result)

