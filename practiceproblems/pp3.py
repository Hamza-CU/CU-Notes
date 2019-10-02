#Problem 5 (Calculating Volume - *)

print("Hello, this is a calculator for the volume of a cone")
print("Please input the 2 dimensions for your cone without units\n")

import time
time.sleep(3)

import math
r = float(input("radius\n"))
h = float(input("height\n"))
v = str((h/3)*(r**2)*math.pi)
print("The volume of your cone is " + v + " units cubed")
