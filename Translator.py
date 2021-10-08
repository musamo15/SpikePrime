
import threading
import zmq
import time
import json
import copy
from zmq.sugar.frame import Message
import traceback

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
        self.sendMessage = False
        self.newMessage = None
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
        self.thread = None
        self.newData = None
        
    def run(self):
        """ Method that runs forever """
        try:
            currentVal = True
            while currentVal:
                # Handle Recieve
                try:
                    self.newData = self.socket.recv(copy=True)

                    # Handle Send
                    if self.sendMessage == True:
                        print("Sending new Data to python")
                        self.socket.send_string(str(json.dumps(self.newMessage)))
                        self.sendMessage = False
                    else:
                        self.socket.send_string("Recieved Message")
                    currentVal = False
                except Exception:
                    print("Exception On Message Thread")
                    self.socket.close(linger=1000)
        except Exception:
            print("Exiting Application")
            self.socket.close(linger=1000)
    
    def getMessage(self,type):
        self.thread = threading.Thread(target=self.run, args=(),daemon=False)
        self.thread.start()                                 
        self.thread.join()
        if self.newData != None:
            self.handleDataFromUnity(self.newData)
        return self.messageDict[type]

    def sendMessageToUnity(self,dictionary):
        self.sendMessage = True
        self.newMessage = dictionary
        self.thread = threading.Thread(target=self.run, args=(),daemon=False)
        self.thread.start()                                 
        self.thread.join()
      
           
    def handleDataFromUnity(self,message):
        # try:
        #     for message in message.split(','):
        #         dict = eval(message)
        #         print(dict)
        #         for key in dict.keys():
        #             self.messageDict[key] = dict[key]
        # except Exception:
        #     print("Exception While Parsing Data")
        try:
           dict = eval(message)
           for key in dict.keys():
                self.messageDict[key] = dict[key]
        except Exception:
            print("Exception While Parsing Data")