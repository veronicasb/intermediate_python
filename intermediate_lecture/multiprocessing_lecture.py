from multiprocessing import Process, Value, Array, Lock, Queue
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
# using queues (must be from multiprocessing module; for process-safe data exchanges)
# using process pool to manage multiple processes
# threading: share data using a global variable
'''
processes: since processes dont exist in the same memory space, they dont have access 
to the same public data, so they need special memory objects --> a Value (for a single value) 
or an Array (for multiple values)
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





