#!/usr/bin/python3
from spike import ColorSensor

# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Measure the color

color = paper_scanner.get_color()


# Print the color name to the console

print('Detected:', color)


# Check if it's a specific color

if color == 'red':
    print('It is red!')
