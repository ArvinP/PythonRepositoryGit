from threading import *
from time import *


class My_thread(Thread):
    def run(self):
        for i in range(100):
            print("Message from My_Thread: ", i)
            sleep(1)


class Your_thread(Thread):
    def run(self):
        for i in range(100):
            print("Message from Your_Thread: ", i)
            sleep(1)


t1 = My_thread()
t2 = Your_thread()

t1.start()
t2.start()

t1.join()
t2.join()
print("Bye")