class Motor:

    def __init__(self,id,speed,rotation,stopAction):
        self.id = id
        self.speed = speed
        self.rotation = rotation
        self.stopAction = stopAction
        self.unit = "cm"
        self.currentMessageDict = {}
    def setRotation(self,rotation,unit):
        if self.rotation != rotation:
            self.rotation = rotation
        if self.unit != unit:
            self.unit = unit
    def setSpeed(self,newSpeed):
        if isinstance(newSpeed,int):
            if self.speed != newSpeed:
                self.speed = newSpeed
        else:
            raise Exception("Type Error, The new speed is not an int")
        

    def setUnit(self,newUnit):
        if isinstance(newUnit,str):
            if self.unit != newUnit:
                self.unit = newUnit
        else:
            raise Exception("Type Error, the new unit is not a string")

    def setStopAction(self,stopAction):
        actions = ["coast", "brake", "hold"]
        if isinstance(stopAction,str):
                if stopAction in actions:
                    if self.stopAction != stopAction:
                        self.stopAction = stopAction
                else:
                    raise Exception("Stop action is not valid (coast, brake, or hold")
        else:
            raise Exception("Type Error, the new stop action is not a string")
    
    def set_degrees_counted(degrees):
        degrees_counted = degrees

    def set_default_speed(speed):
        #sets default motor speed??
        return

    #Sets whether or not stall detection is on
    #Stall detection turns motor off if it gets stuck, powers off after 2 seconds
    #True - stall detection on (Default), False - stall detection off  
    def set_stall_detection(self, stallValue):
        if isinstance(stallValue, bool):
            self.stallDetect = stallValue
        else:
            raise Exception("TypeError, stallValue is not a boolean") 

    def get_id(self):
        return self.id
    
    def get_speed(self):
        return self.speed    

    def get_rotation(self):
        return self.rotation

    def get_position(self):
        return #POSITION FROM UNITY SIM

    def get_degrees_counted(self):
        return #DEGREES COUNTED FROM UNITY

    def get_default_speed():
        return #SPEED OF DEFAULT MOTOR??

    #json being sent to unity 
    def get_messageDict(self,amount,steering):
        dict = {
            "id":self.getId(),
            "amount":amount,
            "rotation":self.getRotation(),
            "speed":self.getSpeed(),            
            "unit":self.getUnit(),
            "steering":steering,
            "stall":"true"
        }
        return dict   

    def send_message(self,newDict):
        isValid = False
        if isinstance(newDict,dict):
            if self.currentMessageDict != newDict:
                self.currentMessageDict = newDict
                isValid = True
        return isValid

    def run_to_position(degrees, direction, speed):
        #runs motor to an absolute position
        #NEED DATA FROM UNITY
        return

    def run_to_degrees_counted(degrees, speed):
        #runs motor until # of degrees counted is equal to degrees parameter
        #UNITY DATA
        return

    def run_for_degrees(degrees, speed):
        #runs motor for a specified # of degrees
        #UNITY DATA 
        return

    def run_for_rotations(rotations, speed):
        #runs motor for specified # of rotations
        #UNITY DATA
        return

    def run_for_seconds(seconds, speed):
        #runs motor for specified # of seconds
        #UNITY DATA
        return

    #starts the motor
    #SEND START SIGNAL TO UNITY
    def start(self,amount,unit,steering,speed):
        if isinstance(steering,int):
            if steering < -100 and steering > 100:
                raise Exception("ValueError, The value of steering is not within -100 to 100")
        else:
                raise Exception("TypeError, steering is not an int")

        self.setUnit(unit)
        self.setSpeed(speed)

        motorDict = self.getMessageDict(amount, steering)
        if self.sendMessage(motorDict):
            print(motorDict)

    #stops the motor
    #SEND STOP SIGNAL TO UNITY
    def stop(self):
        for i in range(self.speed, 0, -1):
            self.speed -= 1

    def start_at_power(power):
        #starts at specified power level
        #do we need this?
        return

    def was_interrupted():
        return #BOOL- whether or not motor was interrupted

    def was_stalled():
        return #BOOL- whether or not motor was stalled