#!/usr/bin/python
from _typeshed import Self
import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')
            time.sleep(self.interval)
    def newMethod(self):
        print("Executing New Function")
example = ThreadingExample()
time.sleep(3)
print('Checkpoint')
time.sleep(3)
print('Bye')

