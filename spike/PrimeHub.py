from .Translator import Translator

class PrimeHub:
    __instance = None
    def __init__(self):
        PrimeHub.__instance = self
        self.motion_sensor = motionSensor()
        print("Created Prime Hub")
    
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if PrimeHub.__instance == None:
         raise Exception("Theres no hub")
      return PrimeHub.__instance

class motionSensor():
    def __init__(self):
        self.__yaw = 0
        self.__translator = Translator.getInstance()

    def get_yaw_angle(self):
        yawDict = self.__translator.getMessage("hub")
        messageYaw = yawDict["rotation"]

        if self.__yaw != messageYaw:
            self.__yaw = messageYaw
        return int(self.__yaw)