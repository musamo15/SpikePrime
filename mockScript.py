#!/usr/bin/python3
from ColorSensor import ColorSensor
from Motor import Motor
from spike import PrimeHub

hub = PrimeHub()

motor = Motor("A")
motor.start()

