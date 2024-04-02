import threading
from threading import *
from time import sleep

def my_method():
    for i in range(10):
        print("My method is running: ", i)
        sleep(0.5)

def your_method():
    for i in range(10):
        print("Your method is running: ", i)
        sleep(0.5)

thread1 = threading.Thread(target=my_method)
thread2 = threading.Thread(target=your_method)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Bye")