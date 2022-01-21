#!/usr/bin/python3

from spike import PrimeHub,Motor,ColorSensor,DistanceSensor

hub = PrimeHub()

colorC = ColorSensor("C")


hub.light_matrix.show_image("Heart")
