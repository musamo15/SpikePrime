#!/usr/bin/python3
from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()

cs = ColorSensor("A")
ds = DistanceSensor("A")


lMotor = Motor("A")
rMotor = Motor("B")


while(ds.get_distance_cm() > 20):
    lMotor.start(15)
    rMotor.start(15)
    

while(hub.motion_sensor.get_yaw_angle() < 90 or hub.motion_sensor.get_yaw_angle() > 350):
    lMotor.start(10)
    rMotor.start(-10)

while(ds.get_distance_cm() > 20):
    lMotor.start(20)
    rMotor.start(20)


while(hub.motion_sensor.get_yaw_angle() > 2):
    lMotor.start(-5)
    rMotor.start(5)

lMotor.start(100)
rMotor.start(100)


    





