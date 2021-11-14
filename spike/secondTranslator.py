import threading
import json
import socket

class Translator():

    __instance = None

    def __init__(self):
        """
        {
            message header: Request, Send

        }
        """
        if Translator.__instance != None:
            raise Exception("This class is a singleton!")
        else:
             Translator.__instance = self
        self.__port = 5000
        self.__host = '127.0.0.1'
        self.__messageDict = {
            "type": None,
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

        self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        notConnected  = True
        print("Waiting to be connected")
        while notConnected:
            try:
                self.__socket.connect((self.__host,self.__port))
                notConnected = False
            except:
                pass

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Translator.__instance == None:
         Translator()
      return Translator.__instance


    def __requestMessage(self):
            newMessage = {
                "requestMessage": 
                {
                    "type": "color"
                }
            }
            try:
                self.__socket.sendall(json.dumps(newMessage).encode('utf-8'))
                self.__newData = self.__socket.recv(1024)
            except:
                print("Unable To Communicate With Unity")
                raise Exception
            
    def __sendMessage(self,newMessage):
        # try:
        #     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcpSocket:
        #         tcpSocket.connect((self.__host,self.__port))
        #         tcpSocket.send_string(json.dumps(newMessage))
        # except Exception:
            
        #     print("Unable To Communicate With Unity")
        pass
    def __handleDataFromUnity(self,message):
        print(message)
        try:
            dict = eval(message)
            for i in dict:
                for key in i.keys():
                    self.__messageDict[key] = i[key]
        except Exception:
            print("Exception While Parsing Data")  

    def getMessageFromUnity(self,type):
        self.__thread = threading.Thread(target=self.__requestMessage, args=(),daemon=False)
        self.__thread.start()                                 
        self.__thread.join()
        if self.__newData != None:
            self.__handleDataFromUnity(self.__newData)
        return self.__messageDict[type]
        # with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        #     s.connect((host,sPort))
        #     s.sendall(b'Hello World')
        #     data = s.recv(1024)

    def sendMessageToUnity(self,newMessage):
        self.__thread = threading.Thread(target=self.__sendMessage, args=(newMessage),daemon=False)
        self.__thread.start()                                 
        self.__thread.join()