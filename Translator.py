
import threading
import zmq
import time

class translator():
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        port = 5556
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % port)

        self.messageDict = {
            
            "color" : {
                "currentColor" : None
            },
            
            "motor" : {
                "amount": 0,
                "rotation": 0,
                "speed": 0,            
                "unit": 0,
                "steering": 0
            }
        }
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
    
    def run(self):
        """ Method that runs forever """
        try:
            while True:
                # Handle Recieve
                print("Recieving Messages: ") 
                self.messageDict["color"]["currentColor"] = "Blue"
                self.messageDict = self.socket.recv_json()   
                
                # Handle Send
                self.socket.send_string("Recieved ")
        except KeyboardInterrupt:
            print("Exiting Application")
    
    def getMessage(self,type):
        print("Here")
        time.sleep(2)
        return self.messageDict[type]


if __name__ == "__main__":
    print("Hello from main method")
    translator = translator()
