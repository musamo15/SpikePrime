from .Translator import Translator

class PrimeHub:
    __instance = None
    def __init__(self):
        PrimeHub.__instance = self
        self.motion_sensor = MotionSensor()
        self.light_matrix  = LightMatrix()
        print("Created Prime Hub")
    
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if PrimeHub.__instance == None:
         raise Exception("PrimeHub Instance Does Not Exist")
      return PrimeHub.__instance

class MotionSensor():
    def __init__(self):
        self.__yaw = 0
        self.__translator = Translator.getInstance()
        
    def get_yaw_angle(self):
        messageDict = {
            "messageType": "hub",
            "messageRequestType":"Request",
            "component": "yaw"
        }
        yawDict = self.__translator.getMessageFromUnity(messageDict)
        if yawDict == None:
            return None
        else:
            messageYaw = yawDict["rotation"]
            if self.__yaw != messageYaw:
                self.__yaw = messageYaw
            return int(self.__yaw)

class LightMatrix():
    def __init__(self):
        self.__translator = Translator.getInstance()
        self.__currentText = None
        self.__currentImage = None
    def write(self,text):
        if text != self.__currentText:
            self.__currentText = text
            # Send message to unity
            lightMatrixMessageDict = { 
                "messageType": "lightMatrix",
                "text":  self.__currentText,
                "image": self.__currentImage
            }
            self.__translator.sendMessageToUnity(lightMatrixMessageDict)
    def show_image(self,image,brightness=100):
        if image != self.__currentImage:
            self.__currentImage = image
            # Send message to unity
            lightMatrixMessageDict = {
                "messageType": "lightMatrix",
                "text":  self.__currentText,
                "image": self.__currentImage
            }
            self.__translator.sendMessageToUnity(lightMatrixMessageDict)
    
