import threading
import json
import socket
import os

class Translator():

    __instance = None
    __requestResponseServer = None
    __shutDownServer = None
    
    def __init__(self):
        if Translator.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Translator.__instance = self
        
        if  Translator.__shutDownServer == None:
            Translator.__shutDownServer = Translator.__ShutDownServer()
        
        if Translator.__requestResponseServer == None:
            Translator.__requestResponseServer = Translator.__RequestResponseServer()

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Translator.__instance == None:
        Translator()
      return Translator.__instance

    def getMessageFromUnity(self,messageDict):
        sensorMessageDict = self.__requestResponseServer.getMessageFromUnity(messageDict)
        if sensorMessageDict != None:
            return sensorMessageDict[messageDict["messageType"]]
        else:
            return None

    def sendMessageToUnity(self,newMessage):
        self.__requestResponseServer.sendMessageToUnity(newMessage)
    
        
    class __RequestResponseServer():
        def __init__(self):
       
            self.__requestResponsePort = 3000
        
            self.__host = '127.0.0.1'
            self.__newData = None
            self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            notConnected  = True
       
            print("Waiting to be connected")
            while notConnected:
                try:
                    self.__socket.connect((self.__host,self.__requestResponsePort))
                    notConnected = False
                except:
                    pass
            self.__socket.settimeout(20.0)
            print("Connected to Unity Simulation")

        def __requestMessage(self,messageDict):
            try:
                self.__socket.sendall(json.dumps(messageDict).encode('utf-8'))
                self.__newData = self.__socket.recv(1024)
            except:
                self.__newData = None
                print("Unable To Communicate With Unity1")
                raise SystemExit
            
        def __sendMessage(self,newMessage):
            """
            "messageType": "[color,motor,ultrasonic,shutdown]",
                "messageRequestType": "[Request,Send]",
                "id": ""
            """
            try:
                self.__socket.sendall(json.dumps(newMessage).encode('utf-8'))
                self.__socket.recv(1024)
            except:
                # raise Exception
                print("Unable To Communicate With Unity2")
                # self.cleanSocket()
                raise SystemExit
            
        def __handleDataFromUnity(self,message):
            """
            One of these 
            
             "motor" : {
                    "stall":None,
                    "currentPosition":None
                }
            "color" : {
                    "currentColor" : "Blue"
                },
            "hub" : {
                    "rotation":None,
                    "distance":None
                 }
            """
            try:
                return eval(message)
            except Exception:
                return None

        def getMessageFromUnity(self,messageDict):
            """
            "messageType": "[color,motor,ultrasonic]",
            "messageRequestType": "[Request,Send]",
            "id": ""
            """
            self.__requestMessage(messageDict)
            if self.__newData != None:
                return self.__handleDataFromUnity(self.__newData)
            else:
                return None
          
        def sendMessageToUnity(self,newMessage):
            self.__sendMessage(newMessage)

        def sendShutDownMessage(self):
            messageDict = {
                "messageType": "shutdown",
                "messageRequestType": "Send"
            }
            self.__sendMessage(messageDict)

    class __ShutDownServer():
        def __init__(self):
            self.__shutdownListenPort = 4444
            self.__host = '127.0.0.1'
            self.__thread = threading.Thread(target=self.__listenForShutdown, args=(),daemon=True)
            self.__thread.start()  
            
        def __listenForShutdown(self):
            print("Shutdown starting: ")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.__host, self.__shutdownListenPort))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(addr)
                    conn.recv(1024)

                    print("Recieved Shutdown Request From Unity")
                    os._exit(1)       

        # def __handleShutdownMessage(self,message):
        #     if message == "Shutdown":
        #         print("Recieved Shutdown Request From Unity")
        #         os._exit(1)                
        