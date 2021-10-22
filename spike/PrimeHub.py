from .Translator import Translator

class PrimeHub:
    __instance = None
    def __init__(self):
        PrimeHub.__instance = self
        print("Created Prime Hub")
        self.Translator = Translator.getInstance()
        self.motion_sensor = self.motionSensor()

    
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if PrimeHub.__instance == None:
         raise Exception("Theres no hub")
      return PrimeHub.__instance

    class motionSensor:
        def __init__(self):
            self.yaw = 0
            self.translator = Translator.getInstance()

        def get_yaw_angle(self):
            yawDict = self.translator.getMessage("hub")
            messageYaw = yawDict["rotation"]

            if self.yaw != messageYaw:
                self.yaw = messageYaw
            return int(self.yaw)