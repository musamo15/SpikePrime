import threading
import json
import socket
import os
import logging

"""
    This static class is the sole communicator between python and the simulation
"""
class Translator():  

    __instance = None
    __requestResponseServer = None
    __shutDownServer = None
    
    def __init__(self):
        if Translator.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Translator.__instance = self
            with open('SpikePrimeLogger.log','w'):
                pass
            logging.basicConfig(filename='SpikePrimeLogger.log',level = logging.DEBUG,format='%(asctime)s %(message)s')
        
        if  Translator.__shutDownServer == None:
            Translator.__shutDownServer = Translator.__ShutDownServer()
        
        if Translator.__requestResponseServer == None:
            Translator.__requestResponseServer = Translator.__RequestResponseServer()

    """
        Returns an instance of the translator
    """
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Translator.__instance == None:
            Translator()
        return Translator.__instance

    """
        Retrieves a requested message from the simulation
        The simulation returns a dictionary specific to the sensor
        Note if the simulation returns an invalid value, None is returned
    """
    def getMessageFromUnity(self,messageDict):
        sensorMessageDict = self.__requestResponseServer.getMessageFromUnity(messageDict)
        if sensorMessageDict != None:
            return sensorMessageDict[messageDict["messageType"]]
        else:
            return None

    """
        Sends a message to the simualtion
        Note the message follows specific structures based on each sensor
        An invalid message structure will lead to loss of data or invalid functionality
    """
    def sendMessageToUnity(self,newMessage):
        self.__requestResponseServer.sendMessageToUnity(newMessage)
    
    """
        This inner class uses sockets to communicate with the simulation.
        Note that the communication is over port 3000 within localhost.
    """
    class __RequestResponseServer():
        def __init__(self):
            self.__requestResponsePort = 3000
            self.__host = '127.0.0.1'
            self.__newData = None
            self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            # Tcp sockets are typically not reusable up to four minutes
            # This following allows the socket connection to be resuable
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # This ensures that a connection is made to the simulation before proceeding
            notConnected  = True
            logging.info("Waiting to be connected, on port %s", self.__requestResponsePort)
            print("Waiting to be connected")
            while notConnected:
                try:
                    self.__socket.connect((self.__host,self.__requestResponsePort))
                    notConnected = False
                except:
                    pass
            # Messages will timeout after a 20 seconds of not getting a response
            self.__socket.settimeout(20.0)
            logging.info("Connected on port %s", self.__requestResponsePort)
            print("Connected to Unity Simulation")

        """
            Requests a message from unity, the dictionary is converted into a json string.
            The socket waits 20 seconds for a response message
        """
        def __requestMessage(self,messageDict):
            """
                The message dictionary should be the following: 
                    "messageType": "[color,motor,ultrasonic,shutdown]",
                    "messageRequestType": "[Request,Send]",
                    "id": ""
            """
            try:
                logging.info("Sending message %s", messageDict)
                self.__socket.sendall(json.dumps(messageDict).encode('utf-8'))
                self.__newData = self.__socket.recv(1024)
                logging.info("Recieved Message from Unity")
            except:
                logging.warn("Did not get a response Message from Unity while requesting a message")
                self.__newData = None
                print("Unable To Communicate With Unity")
                raise SystemExit
        
        """
            Sends a message from unity, the dictionary is converted into a json string.
            The socket waits 20 seconds for a response message
            Note a response is required so that consecutive messages are not sent together
        """    
        def __sendMessage(self,messageDict):
            """
                The message dictionary should be the following: 
                    "messageType": "[color,motor,ultrasonic,shutdown]",
                    "messageRequestType": "[Request,Send]",
                    "id": ""
            """
            try:
                logging.info("Sending message", messageDict)
                self.__socket.sendall(json.dumps(messageDict).encode('utf-8'))
                logging.info("Recieved Message from Unity")
                recievedMessage = self.__socket.recv(1024)
                self.checkForInvalidPort(recievedMessage)
            except:
                logging.warn("Did not get a response Message from Unity while sending a message")
                print("Unable To Communicate With Unity")
                raise SystemExit
        """
            Handles the recieved request response from the simulation
        """  
        def __handleDataFromUnity(self,message):
            """
                One of the following is expected from the message parameter:
                "motor" : {
                    "stall":None,
                    "currentPosition":None
                }

                "color" : {
                    "currentColor" : "Blue"
                }
                
                "hub" : {
                    "rotation":None,
                    "distance":None
                }
            """
            self.checkForInvalidPort(message)
            try:
                return eval(message)
            except Exception:
                return None
        """
            Retrieves the message response from the request
            Note None is returned if the simulation does not return a valid value
        """
        def getMessageFromUnity(self,messageDict):
            self.__requestMessage(messageDict)
            if self.__newData != None:
                return self.__handleDataFromUnity(self.__newData)
            else:
                return None
        
        """
            Sends the message to the simulation
        """  
        def sendMessageToUnity(self,newMessage):
            self.__sendMessage(newMessage)

        def checkForInvalidPort(self,message):
            dict = eval(message)
            if "error" in dict:
                errorMessage = dict["error"]["message"]
                logging.warn(str(errorMessage))
                print(errorMessage)
                raise SystemExit
            
    """
        This inner class starts a daemon thread which listens for shutdown request 
        from the simulation.
        Once a shutdown request is recieved, the python application quits
        Daemon threads are spawned from the main thread and killed off after the application quits
        Note that the communication is over port 4444 within localhost
    """
    class __ShutDownServer():
        def __init__(self):
            self.__shutdownListenPort = 4444
            self.__host = '127.0.0.1'
            self.__thread = threading.Thread(target=self.__listenForShutdown, args=(),daemon=True)
            self.__thread.start()  
        
        """
            Listens for a shutdown request
        """
        def __listenForShutdown(self):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.__host, self.__shutdownListenPort))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print("Recieved Shutdown Request From the Simulation")
                    conn.recv(1024)
                    os._exit(1)
     