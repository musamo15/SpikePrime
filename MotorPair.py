from Motor import Motor
import math
import json

class MotorPair:

    def __init__(self,leftMotorId,rightMotorId):
        # Creating a left motor with an Id, speed of 2, rotation of 17.6pi, and stopaction of hold 
        self.leftMotor = Motor(leftMotorId,2,17.6 * math.pi,"hold")
        # Creating a right motor with an Id, speed of 2, rotation of 17.6pi, and stopaction of hold 
        self.rightMotor = Motor(rightMotorId,2,17.6 * math.pi,"hold")

    def set_motor_rotation(self,amount,unit):
         self.leftMotor.setRotation(amount,unit)
         self.rightMotor.setRotation(amount,unit)

    def set_default_speed(self,speed):
        self.leftMotor.setSpeed(speed)
        self.rightMotor.setSpeed(speed)

    def set_stop_action(self,action):
        self.leftMotor.setStopAction(action)
        self.rightMotor.setStopAction(action)

    def get_default_speed(self):
        return self.leftMotor.getSpeed()
    
    def move(self,amount,unit,steering,speed):
        # Steering = 0 -> Go Straight
        # Steering = -100 -> Go Left
        # Steering = 100 -> Go Right
        if isinstance(steering,int):
            if steering < -100 and steering > 100:
                raise Exception("ValueError, The value of steering is not within -100 to 100")    
        else:
            raise Exception("TypeError, Steering is not an int") 

        self.leftMotor.setUnit(unit)
        self.rightMotor.setUnit(unit)
        self.leftMotor.setSpeed(speed)
        self.rightMotor.setSpeed(speed)

        leftMotorDict = self.leftMotor.getMessageDict(amount,steering)
        rightMotorDict = self.rightMotor.getMessageDict(amount,steering)
        if self.leftMotor.sendMessage(leftMotorDict):
            #Construct Message
            print(leftMotorDict)
            
        if self.rightMotor.sendMessage(rightMotorDict):
            #Construct Message
            print(leftMotorDict)

        """
        leftMotor = {
            "id":self.leftMotor.getId(),
            "amount":amount,
            "rotation":self.leftMotor.getRotation(),
            "speed":self.leftMotor.getSpeed(),            
            "unit":self.leftMotor.getUnit(),
            "steering":steering
        }
        """


