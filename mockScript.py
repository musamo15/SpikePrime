#!/usr/bin/python3
from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()

cs = ColorSensor("A")
ds = DistanceSensor("A")


lMotor = Motor("A")
rMotor = Motor("B")

lMotor.start(15)
rMotor.start(15)


while(True):
    
    #When we are within 10cm of the first wall
    if(ds.get_distance_cm() < 20):

        #We turn until we are facing ~90 degrees
        while(hub.motion_sensor.get_yaw_angle() < 90 or hub.motion_sensor.get_yaw_angle() == 360):
            lMotor.start(15)
            rMotor.start(-15)

        #Start moving forward again
        while(ds.get_distance_cm() > 20):
            rMotor.start(15)
            lMotor.start(15)
        
        while(hub.motion_sensor.get_yaw_angle() > 1):
            rMotor.start(15)
            lMotor.start(-15)

        lMotor.start(100)
        rMotor.start(100)
        break
