from .Translator import Translator
from .PrimeHub import PrimeHub

"""
    This library represents the motor sensor of the spike prime library
"""
class Motor:
    def __init__(self,id):
        PrimeHub.getInstance()
        self.__translator = Translator.getInstance()
        self.__id = id
        self.__speed = None
        self.__rotation = 0.0
        self.__stopAction = "brake"
        self.__unit = "rotations"
        self.__defaultSpeed = 75
        self.__position = (0,0,0)
        self.__stallDetect = False
        self.__currentMessageDict = {}
    
    """
        Sets the speed of the motor
    """     
    def __set_speed(self,newSpeed):
        if isinstance(newSpeed,int):
            if newSpeed >= -100 and newSpeed <= 100:
                if self.__speed != newSpeed:
                    self.__speed = newSpeed
        else:
            raise Exception("Type Error, The new speed is not an int")

    """
        Sets the stop action of the motor, the valid values are "coast","brake","hold"
    """
    def set_stop_action(self,stopAction):
        if isinstance(stopAction,str):
                actions = ["coast", "brake", "hold"]
                if stopAction in actions:
                    if self.__stopAction != stopAction:
                        self.__stopAction = stopAction
                else:
                    raise Exception("ValueError, action is not one of the allowed values (coast, brake, or hold)")
        else:
            raise Exception("TypeError, the new stop action is not a string")
    
    """
        Sets the default speed of the motor, note the valid values for speed are -100 to 100
    """
    def set_default_speed(self, newDefSpeed):
        if isinstance(newDefSpeed, int):
            if newDefSpeed >= -100 and newDefSpeed <= 100:
                if self.__defaultSpeed != newDefSpeed:
                    self.__defaultSpeed = newDefSpeed
        else:
            raise Exception("TypeError, default_speed is not an integer")

    """
        Sets whether or not stall detection is on
        Stall detection turns motor off if it gets stuck, powers off after 2 seconds
    """
    def set_stall_detection(self, stallValue):
        if isinstance(stallValue, bool):
            self.__stallDetect = stallValue
        else:
            raise Exception("TypeError, stallValue is not a boolean") 

    """
        Returns the id of the motor sensor, the id is associated with the port.
    """
    def __get_id(self):
        return self.__id
    
    """
        Returns the current speed of the motor
    """
    def get_speed(self):
        if self.__speed == None:
            return self.__defaultSpeed
        return self.__speed    

    """
        Returns the current speed of the motor
    """
    def __get_rotation(self):
        return self.__rotation

    """
        Gets the position of the robot
    """
    def get_position(self):
        messageDict = {
            "messageType": "motor",
            "messageRequestType": "Request",
            "id": self.__get_id(),
            "component": "position"
        }
        motorDict = self.__translator.getMessageFromUnity(messageDict) 
        if motorDict == None:
            return None
        else:
            currentPos = motorDict["currentPosition"]
            if currentPos != self.__position:
                self.__position = currentPos
            return self.__position 
    """
        Returns the default speed of the robot
    """
    def get_default_speed(self):
        
        return self.__defaultSpeed
    
    """
        Constructs a message dictionary with the specified values held within the motor object
    """
    def __get_messageDict(self,amount=0,steering=0):
        dict = {
            "messageType": "motor",
            "messageRequestType": "Send",
            "id": self.__get_id(),
            "amount": amount,
            "rotation": self.__get_rotation(),
            "speed": self.get_speed(),            
            "unit": self.__unit,
            "steering": steering,
            "stall": self.__stallDetect,
            "stopAction": self.__stopAction
        }
        return dict   

    """
        Checks if the new message sent is different than the most recent motor message.
    """
    def __should_send_message(self,newDict):
        isValid = False
        if isinstance(newDict,dict):
            if self.__currentMessageDict != newDict:
                self.__currentMessageDict = newDict
                isValid = True
        return isValid

    """
        Send a motor message to the simulation with a specified speed.
    """
    def __sendMotorMessage(self,speed):
        self.__set_speed(speed)
        motorDict = self.__get_messageDict()
        if  self.__should_send_message(motorDict) == True:
            self.__translator.sendMessageToUnity(motorDict)

    """
        Starts the motor with a specified speed or a default of 75.
    """
    def start(self,speed = None):
        if speed == None:
             self.__sendMotorMessage(self.get_default_speed())
        else:
            self.__sendMotorMessage(speed)

    """
        Stops the motor
    """
    def stop(self):
        self.__sendMotorMessage(0)

    """
        Returns true if the motor was stalled        
    """
    def was_stalled(self):
        isValid = False
        if self.__stallDetect == True:
            messageDict = {
                "messageType": "motor",
                "messageRequestType": "Request",
                "id": self.__get_id(),
                "component": "stall"
            }
            motorDict = self.__translator.getMessageFromUnity(messageDict)
            if motorDict == None:
                return None
            else:
                if motorDict["stall"] == "True":
                    isValid = True
        return isValid
    
    """
    The following methods are currently not implemented.
    
    def __get_unit(self):
        return self.__unit
    
    def __set_unit(self,newUnit):
        if isinstance(newUnit,str):
            if self.__unit != newUnit:
                self.__unit = newUnit
        else:
            raise Exception("Type Error, the new unit is not a string")
    
    def __set_rotations(self,rotation,unit):
        if self.__rotation != rotation:
            self.__rotation = rotation
        if self.__unit != unit:
            self.__unit = unit
    
    #Starts at specified power level
    def start_at_power(power):
        pass
    #Returns whether or not motor was interrupted
    def was_interrupted():
        pass    
    #Runs motor for specified # of seconds
    def run_for_seconds(self, seconds, speed):
        pass  
    #Runs motor for specified # of rotations
    def run_for_rotations(self, rotations, speed):
        if isinstance(rotations, float):
            if isinstance(speed, int):
                self.__set_unit("rotations")
                self.__set_rotations(rotations)
                self.start(speed)
            else:
                raise Exception("TypeError, speed is not an int")
        else:
            raise Exception("TypeError, rotations is not a float")
        
    #Runs motor for specified # of rotations
    def run_for_rotations(self, rotations, speed):
        if isinstance(rotations, float):
            if isinstance(speed, int):
                self.__set_unit("rotations")
                self.__set_rotations(rotations)
                self.start(speed)
            else:
                raise Exception("TypeError, speed is not an int")
        else:
            raise Exception("TypeError, rotations is not a float")
    
    #Runs motor for a specified # of degrees
    def run_for_degrees(self,degrees, speed):
        pass
    
     #Runs motor to an absolute position (rotates motor X degrees), degrees 0-359
    #"Shortest path", "Clockwise", "Counterclockwise" are options for direction.
    def run_to_position(self,degrees, direction, speed):
        pass

    #Runs motor until # of degrees counted is equal to degrees parameter
    def run_to_degrees_counted(self,degrees,speed):
        if isinstance(degrees, int):
            if isinstance(speed, int):
                self.__set_unit("degrees")
                self.set_degrees_counted(degrees)
                self.start(speed)
            else:
                raise Exception("TypeError, speed is not an integer")
        else:
            raise Exception("TypeError, degrees is not an integer")
        
    def get_degrees_counted(self):
        pass
    
    def set_degrees_counted(self,degrees):
        pass
        
    """