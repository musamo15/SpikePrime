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
        self.keepRunning = True
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        try:
            while True:
                # Do something
                print(str(self.keepRunning))
                if self.keepRunning:
                    print('Doing something imporant in the background')
                    time.sleep(self.interval)
                else:
                    raise InterruptedError            
        except InterruptedError:
            self.spawnNewThread(self.newMethod)
                
    
    def spawnNewThread(self,target,newArgs=None):
        print("here")
        if newArgs == None:
            print("None")
            self.thread = threading.Thread(target=self.run, args=())
        else:
            self.thread = threading.Thread(target=self.run, args=newArgs)
        self.thread.daemon = True
        self.keepRunning = True
        self.thread.start()  
    
    def newMethod(self):
        print("Executing New Function")
example = ThreadingExample()
time.sleep(3)
example.keepRunning = False
print('Checkpoint')
time.sleep(3)
print('Bye')

