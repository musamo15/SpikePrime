from .Translator import Translator

"""
    The primehub class represent the spike prime primehub object 
    with a motion sensor and light matrix.
"""
class PrimeHub:
    __instance = None
    def __init__(self):
        PrimeHub.__instance = self
        self.motion_sensor = MotionSensor()
        self.light_matrix  = LightMatrix()
        print("Created Prime Hub")

    """
        The purpose of this method is to verify that an instance of spike prime is created,
        before a sensor is initialized
        Raises:
            Exception: If a primehub was not created
        Returns:
            the static instance of primehub
    """
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if PrimeHub.__instance == None:
         raise Exception("PrimeHub Instance Does Not Exist")
      return PrimeHub.__instance

"""
    The motion sensor class represents the current motion of the spike prime robot.
    The motion of the robot is represented by the yaw, roll and pitch angles of the robot.
"""
class MotionSensor():
    def __init__(self):
        self.__yaw = 0
        self.__roll = 0
        self.__pitch = 0
        self.__translator = Translator.getInstance()
    
    """
        Returns the current yaw of the robot
        The valid values for yaw are (-180 to 180, None)
        Note that a None return value dictates that an invalid value was recieved from the simulation 
    """
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
    """
        Returns the current roll of the robot
        The valid values for roll are (-180 to 180, None)
        Note that a None return value dictates that an invalid value was recieved from the simulation 
    """
    def get_roll_angle(self):
        return 0
        # messageDict = {
        #     "messageType": "hub",
        #     "messageRequestType":"Request",
        #     "component": "roll"
        # }
        # rollDict = self.__translator.getMessageFromUnity(messageDict)
        # if rollDict == None:
        #     return None
        # else:
        #     messageRoll = rollDict["rotation"]
        #     if self.__roll != messageRoll:
        #         self.__roll = messageRoll
        #     return int(self.__roll)
    
    """
        Returns the current pitch of the robot
        The valid values for pitch are (-180 to 180, None)
        Note that a None return value dictates that an invalid value was recieved from the simulation 
    """
    def get_pitch_angle(self):
        return 0
        # messageDict = {
        #     "messageType": "hub",
        #     "messageRequestType":"Request",
        #     "component": "pitch"
        # }
        # pitchDict = self.__translator.getMessageFromUnity(messageDict)
        # if pitchDict == None:
        #     return None
        # else:
        #     messagePitch = pitchDict["rotation"]
        #     if self.__pitch != messagePitch:
        #         self.__pitch = messagePitch
        #     return int(self.__pitch)
    
"""
    The light matrix class represents the current displayed 
    on the light matrix of the spike prime robot.
"""
class LightMatrix():
    def __init__(self):
        self.__translator = Translator.getInstance()
        self.__currentText = None
        self.__currentImage = None
   
    """
        Write a message to the lightMatrix, that is displayed as scrolling text
        Note that the consecutive text wont be sent to the simulation
    """
    def write(self,newText):
        if newText != self.__currentText:
            self.__currentText = newText
            # Send message to unity
            lightMatrixMessageDict = { 
                "messageType": "lightMatrix",
                "text":  self.__currentText,
                "image": self.__currentImage
            }
            self.__translator.sendMessageToUnity(lightMatrixMessageDict)
    """
        Shows an image on the light matrix
        The following images are allowed: Happy, Sad and Heart
        Note that the consecutive images wont be sent to the simulation
    """       
    def show_image(self,image,brightness=100):
        if image != self.__currentImage:
            self.__currentImage = image
            # Send message to unity
            lightMatrixMessageDict = {
                "messageRequestType" : "Send",
                "messageType": "lightMatrix",
                "text":  self.__currentText,
                "image": self.__currentImage
            }
            self.__translator.sendMessageToUnity(lightMatrixMessageDict)
    
