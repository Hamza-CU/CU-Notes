#Problem 4 (Conversion Program - *)

print("Hello, I am a Celsius to Fahrenheit converter")
import time
time.sleep(5)

tempC = int(input("please tell me what temperature it is currently in Celsius \n"))
tempF = str((tempC * 9/5) + 32)

print("the current temperature in the room is "+ tempF + "degrees Fahrenheit")
