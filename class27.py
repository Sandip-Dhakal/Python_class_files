# multiprocessing thread in python
from threading import Thread
import time

# class MyThread(Thread):
#     def __init__(self):
#         super(MyThread, self).__init__()

#     def run(self):
#         while(True):
#             print('I am in a separate Thread')
#             time.sleep(2)

#     def start(self):
#         print('This is start of thread')
#         super(MyThread, self).start()

# thread1 = MyThread()
# thread1.start()

# while(True):
#     print('I am main thread')
#     time.sleep(1)

# print('I am outside inifite loop')

# class MyThread(Thread):
#     def __init__(self, name, id):
#         super(MyThread, self).__init__()
#         self.name = name
#         self.id = id

#     def run(self):
#         # print(self.name,"is running")
#         time.sleep(2)
#         print(self.id, ':', self.name, ":", time.ctime(time.time()))

#     def start(self):
#         # print(self.name,"is started")
#         super(MyThread, self).start()


# # Thread implementation
# thread1 = MyThread('Thread1', 1)
# thread2 = MyThread('Thread2', 2)
# thread3 = MyThread('Thread3', 3)

'''
join() method waits for all threads to be completed which are added to 
thread pool by join method, then only gives output. Join also blocks other thread 
to run unless that thread is completed.
'''

# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# thread3.start()
# thread3.join()

# multiple threads running together
# for x in range(100):
#     name = "Thread"+str(x)
#     thread  = MyThread(name, x)
#     thread.start()


#Thread Synchronization using Lock class og threading
from threading import Lock
class MyThread (Thread):
    
    threadLock = Lock()
    
    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        MyThread.threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        MyThread.threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threads = []

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)

# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")

