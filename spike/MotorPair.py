from .Motor import Motor
import math
from .PrimeHub import PrimeHub

class MotorPair:

    def __init__(self,leftMotorId,rightMotorId):
        PrimeHub.getInstance()
        # Creating a left motor with an Id, speed of 2, rotation of 17.6pi, and stopaction of hold 
        self.leftMotor = Motor(leftMotorId,2,17.6 * math.pi,"hold")
        # Creating a right motor with an Id, speed of 2, rotation of 17.6pi, and stopaction of hold 
        self.rightMotor = Motor(rightMotorId,2,17.6 * math.pi,"hold")
    """
    The following methods are currently not implemented.
    
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

    #move motor pair using differential (tank) steering a certain distance
    def move_tank(amount, unit, left_speed, right_speed):
        return 
        
    #start moving motor pair using differential (tank) steering
    def start_tank(left_speed, right_speed):
        return

    #starts moving driving base at specific power 
    def start_at_power(power, steering):
        return

    #starts moving driving base at specific power for each motor
    def start_tank_at_power(left_power, right_power):
        return     
    """