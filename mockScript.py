#!/usr/bin/python3

from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()

dsFront = DistanceSensor("C")
dsBack = DistanceSensor("F")

lMotor = Motor("B")
rMotor = Motor("A")


lMotor.start(10)
rMotor.start(10)



while True:
    print("Front: ", dsFront.get_distance_cm())
    print("Back: ", dsBack.get_distance_cm())