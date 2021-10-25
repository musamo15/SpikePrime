import threading
import zmq
import json
from zmq.sugar.frame import Message


class Translator():

    __instance = None

    def __init__(self):
        
        if Translator.__instance != None:
            raise Exception("This class is a singleton!")
        else:
             Translator.__instance = self
        port = 5556
        context = zmq.Context()
        self.__socket = context.socket(zmq.REP)
        self.__socket.bind("tcp://*:%s" % port)
        self.__sendMessage = False
        self.__newMessage = None
        self.__messageDict = {
            
            "color" : {
                "currentColor" : None
            },
            "motor" : {
                "stall":None,
                "currentPosition":None
            },
            "hub" : {
                "rotation":None
            },
            "distance" : {
                "value":None
            }
        }
        self.__thread = None
        self.__newData = None

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Translator.__instance == None:
         Translator()
      return Translator.__instance


    def run(self):
        """ Method that runs forever """
        try:
            currentVal = True
            while currentVal:
                # Handle Recieve
                try:
                    self.__newData = self.__socket.recv()

                    # Handle Send
                    if self.__sendMessage == True:
                        print("Sending new Data to python")
                        self.__socket.send_string(json.dumps(self.__newMessage))
                        self.__sendMessage = False
                    else:
                        self.__socket.send_string("Recieved Message")
                    currentVal = False
                except Exception:
                    print("Exception On Message Thread")
                    self.__socket.close(linger=1000)
        except Exception:
            print("Exiting Application")
            self.__socket.close(linger=1000)
    
    def getMessage(self,type):
        self.__thread = threading.Thread(target=self.run, args=(),daemon=False)
        self.__thread.start()                                 
        self.__thread.join()
        if self.__newData != None:
            self.__handleDataFromUnity(self.__newData)
        return self.__messageDict[type]

    def sendMessageToUnity(self,dictionary):
        self.__sendMessage = True
        self.__newMessage = dictionary
        self.__thread = threading.Thread(target=self.run, args=(),daemon=False)
        self.__thread.start()                                 
        self.__thread.join()
      
           
    def __handleDataFromUnity(self,message):

        try:
            dict = eval(message)
            for i in dict:
                for key in i.keys():
                    self.__messageDict[key] = i[key]
        except Exception:
            print("Exception While Parsing Data")  