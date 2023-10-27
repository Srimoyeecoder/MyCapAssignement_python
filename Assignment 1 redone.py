# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:47:53 2023

@author: SRIMOYEE
"""

import math

# Accept the radius from the user
radius = float(input("Input the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")
# Accept the filename from the user
filename = input("Input the Filename: ")

# Split the filename into its base and extension
base, extension = filename.split('.')

# Display the file extension
print(f"The extension of the file is '{extension}'")