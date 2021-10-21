#!/usr/bin/python3
from spike import PrimeHub,Motor,ColorSensor
hub = PrimeHub()

colorSensor = ColorSensor("A")

lMotor = Motor("A")
rMotor = Motor("B")
lMotor.set_default_speed(111110)

lMotor.start(15)
rMotor.start(15)



#Turn right on LightBlue
# while(True):
#     color = colorSensor.get_color()
#     if color == "Light Blue":
#         lMotor.start(15)
        
#Turn left on Blue
# while(True):
#     color = colorSensor.get_color()
#     if color == "Blue":
#         rMotor.start(15)


# #Go backwards on Green
# while(True):
#     color = colorSensor.get_color()
#     if color == "Green":
#         rMotor.start(-10)
#         lMotor.start(-10)

# while(True):
#     color = colorSensor.get_color()
#     if color  == "Violet":
#         lMotor.start(-5)
#         rMotor.start(5)
