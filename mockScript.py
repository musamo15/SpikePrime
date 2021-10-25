#!/usr/bin/python3
from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()

cs = ColorSensor("A")



lMotor = Motor("A")
rMotor = Motor("B")


rMotor.start(15)
print("Hello World")
lMotor.start(15)

    





