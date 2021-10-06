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