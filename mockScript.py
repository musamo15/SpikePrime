#!/usr/bin/python3
from ColorSensor import ColorSensor
from Motor import Motor
from spike import PrimeHub

hub = PrimeHub()

colorSensor = ColorSensor()

lMotor = Motor("A")
rMotor = Motor("B")

lMotor.start(5)
rMotor.start(5)




















# while(True):
#     color = colorSensor.get_color()
#     if color  == "Violet":
#         lMotor.start(-5)
#         rMotor.start(5)
#     # elif color == "":

#     # elif color == "":  
        



