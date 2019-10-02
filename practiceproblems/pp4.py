#Problem 6 (Grade Calculation - *)

print("Hello im your grade calculator, please input your grades as a percentage out of 100")

import time

m1 = float(input("place your first midterm grade here\n"))
time.sleep(2)
m2 = float(input("place your second midterm grade here\n"))
time.sleep(2)
m3 = float(input("place your third midterm grade here\n"))
time.sleep(2)
final = float(input("place your finals grade here\n"))

average = str(((m1 + m2 + m3) * 0.2) + (final * 0.4))
print("your final mark is", average)
