from .Translator import Translator

class Motor:

    def __init__(self,id):
        self.id = id
        self.speed = 0
        self.rotation = 0.0
        self.stopAction = "coast"
        self.unit = "rotations"
        self.currentMessageDict = {}
        self.translator = Translator.getInstance()
        self.default_speed = None
        self.position = (0,0)

    def __set_rotations(self,rotation,unit):
        if self.rotation != rotation:
            self.rotation = rotation
        if self.unit != unit:
            self.unit = unit
            
    def __set_speed(self,newSpeed):
        if isinstance(newSpeed,int):
            if(-100 <= newSpeed <= 100):
                if self.speed != newSpeed:
                    self.speed = newSpeed
        else:
            raise Exception("Type Error, The new speed is not an int")
        
    #need list of acceptable units (rotations,sec,in,cm,degrees?)
    def __set_unit(self,newUnit):
        if isinstance(newUnit,str):
            if self.unit != newUnit:
                self.unit = newUnit
        else:
            raise Exception("Type Error, the new unit is not a string")

    def set_stop_action(self,stopAction):
        actions = ["coast", "brake", "hold"]
        if isinstance(stopAction,str):
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
            if(-100 <= newDefSpeed <= 100):
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
        return self.speed    

    def __get_rotation(self):
        return self.rotation

    def get_position(self):
        motorDict = self.translator.getMessage("position")
        currentPos = motorDict["currentPosition"]

        if currentPos != self.position:
            self.position = currentPos
        return self.position 
        
    def get_degrees_counted(self):
        return #DEGREES COUNTED FROM UNITY

    def get_default_speed(self):
        if(self.default_speed == None):
            print("No default speed")
        else:
            return self.default_speed
    
    #json being sent to unity 
    def __get_messageDict(self,amount=0,steering=0):
        dict = {
            "motorMessage": 
                {
                    "id":self.__get_id(),
                    "amount":amount,
                    "rotation":self.__get_rotation(),
                    "speed":self.get_speed(),            
                    "unit":self.unit,
                    "steering":steering,
                    "stall":"true",
                    "default_speed": self.get_default_speed()
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

    def run_to_position(degrees, direction, speed):
        #runs motor to an absolute position (rotates motor X degrees), degrees 0-359
        #"Shortest path", "Clockwise", "Counterclockwise" are options for direction.
        #NEED DATA FROM UNITY
        return

    def run_to_degrees_counted(self,degrees, speed):
        #runs motor until # of degrees counted is equal to degrees parameter
        if isinstance(degrees, int):
            if isinstance(speed, int):
                self.__set_unit("degrees")
                self.set_degrees_counted(degrees)
                self.start(speed)
            else:
                raise Exception("TypeError, speed is not an integer")
        else:
            raise Exception("TypeError, degrees is not an integer")
        #UNITY DATA

    def run_for_degrees(degrees, speed):
        #runs motor for a specified # of degrees
        #UNITY DATA 
        return

    #runs motor for specified # of rotations
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

    def run_for_seconds(self, seconds, speed):
        #runs motor for specified # of seconds
        #UNITY DATA
        return

    #starts the motor
    #SEND START SIGNAL TO UNITY
    def start(self,speed = None ):

        self.__set_speed(speed)

        motorDict = self.get_messageDict()
        if  self.should_send_message(motorDict) == True:
            self.translator.sendMessageToUnity(motorDict)
    #stops the motor, not very smoothly i think
    #SEND STOP SIGNAL TO UNITY
    def stop(self):
        if(self.stopAction == "hold"):
            #holding will acitvely drive motor to whatever the end condition is
            pass
        elif(self.stopAction == "break"):
            self.__set_speed(0)
        elif(self.stopAction == "coast"):
           #math to make vehicle coast
           pass

    def start_at_power(power):
        #starts at specified power level
        #do we need this?
        return

    def was_interrupted():
        return #BOOL- whether or not motor was interrupted

    #possible int tracker (0,1,2)
    #0 - motor stall detection on, 1 - motor stall detection off, 2 - motor is stalled
    def was_stalled():
        return #BOOL- whether or not motor was stalled