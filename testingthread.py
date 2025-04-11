from threading import Thread
from time import sleep
from CustomThread import CustomThread

from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(1)
    return "aaaa"


if __name__ == "__main__":
    thread = CustomThread(target = threaded_function, args = (10, ))
    thread.start()
    print(thread.join())
    print("thread finished...exiting")