#!/usr/bin/python3
from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()
distanceSensor = DistanceSensor('Z')


lMotor = Motor('A')
rMotor = Motor('B')




hub.light_matrix.show_image('happy')
    
rMotor.start(15)
lMotor.start(15)

while True:

    #When the distance sensor is < 100 cm we make a left turn
    while distanceSensor.get_distance_cm() <= 100:
            rMotor.start(15)
            lMotor.start(-15)
            hub.light_matrix.show_image('sad')


    hub.light_matrix.show_image('heart')
    rMotor.start(15)
    lMotor.start(15)


