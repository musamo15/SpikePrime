from .Translator import Translator
from .PrimeHub import PrimeHub
class Motor:

    def __init__(self,id):
        self.primeHub = PrimeHub.getInstance()
        self.id = id
        self.speed = None
        self.rotation = 0.0
        self.stopAction = "brake"
        self.unit = "rotations"
        self.default_speed = None
        self.position = (0,0)
        self.stallDetect = False
        self.currentMessageDict = {}
        self.translator = Translator.getInstance()

    def __set_rotations(self,rotation,unit):
        if self.rotation != rotation:
            self.rotation = rotation
        if self.unit != unit:
            self.unit = unit
            
    def __set_speed(self,newSpeed):
        if isinstance(newSpeed,int):
            if ( newSpeed >= -100 and newSpeed <= 100):
                if self.speed != newSpeed:
                    self.speed = newSpeed
        else:
            raise Exception("Type Error, The new speed is not an int")
        
    def __set_unit(self,newUnit):
        if isinstance(newUnit,str):
            if self.unit != newUnit:
                self.unit = newUnit
        else:
            raise Exception("Type Error, the new unit is not a string")

    def set_stop_action(self,stopAction):
        
        if isinstance(stopAction,str):
                actions = ["coast", "brake", "hold"]
                if stopAction in actions:
                    if self.stopAction != stopAction:
                        self.stopAction = stopAction
                else:
                    raise Exception("ValueError, action is not one of the allowed values (coast, brake, or hold)")
        else:
            raise Exception("TypeError, the new stop action is not a string")
    
    def set_degrees_counted(self,degrees):
        degrees_counted = degrees

    def set_default_speed(self, newDefSpeed):
        if isinstance(newDefSpeed, int):
            if ( newDefSpeed >= -100 and newDefSpeed <= 100):
                if self.default_speed != newDefSpeed:
                    self.default_speed = newDefSpeed
        else:
            raise Exception("TypeError, default_speed is not an integer")

    #Sets whether or not stall detection is on
    #Stall detection turns motor off if it gets stuck, powers off after 2 seconds
    #True - stall detection on (Default), False - stall detection off  
    def set_stall_detection(self, stallValue):
        if isinstance(stallValue, bool):
            self.stallDetect = stallValue
        else:
            raise Exception("TypeError, stallValue is not a boolean") 

    def __get_id(self):
        return self.id
    
    def get_speed(self):
        if self.speed == None:
            return self.default_speed
        return self.speed    

    def __get_rotation(self):
        return self.rotation

    def __get_unit(self):
        return self.unit

    #Gets position from Unity via JSON data
    def get_position(self):
        motorDict = self.translator.getMessage("motor")
        currentPos = motorDict["currentPosition"]

        if currentPos != self.position:
            self.position = currentPos
        return self.position 
        
    def get_degrees_counted(self):
        pass

    def get_default_speed(self):
        if(self.default_speed == None):
            print("No default speed")
        else:
            return self.default_speed
    
    #JSON being sent to unity 
    def __get_messageDict(self,amount=0,steering=0):
        dict = {
            "motorMessage": 
                {
                    "id": self.__get_id(),
                    "amount": amount,
                    "rotation": self.__get_rotation(),
                    "speed": self.get_speed(),            
                    "unit": self.unit,
                    "steering": steering,
                    "stall": self.stallDetect,
                    "stopAction": self.stopAction
                }
        }
        return dict   

    def __should_send_message(self,newDict):
        isValid = False
        if isinstance(newDict,dict):
            if self.currentMessageDict != newDict:
                self.currentMessageDict = newDict
                isValid = True
        return isValid

    def __sendMotorMessage(self,speed):
        self.__set_speed(speed)
        motorDict = self.__get_messageDict()
        if  self.__should_send_message(motorDict) == True:
            self.translator.sendMessageToUnity(motorDict)

    #Runs motor to an absolute position (rotates motor X degrees), degrees 0-359
    #"Shortest path", "Clockwise", "Counterclockwise" are options for direction.
    def run_to_position(degrees, direction, speed):
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
   
    #Runs motor for a specified # of degrees
    def run_for_degrees(degrees, speed):
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

    #Runs motor for specified # of seconds
    def run_for_seconds(self, seconds, speed):
        pass

    #Starts the motor
    def start(self,speed = 75 ):
        self.__sendMotorMessage(speed)

    #Stops the motor
    def stop(self):
        self.__sendMotorMessage(0)

    #Starts at specified power level
    def start_at_power(power):
        pass

    #Returns whether or not motor was interrupted
    def was_interrupted():
        pass 

    def was_stalled(self):
        isValid = False
        if self.stallDetect == True:
            motorDict = self.translator.getMessage("motor")
            if motorDict["stall"] == "True":
                isValid = True
        return isValid
       
