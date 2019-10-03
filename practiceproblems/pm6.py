import math

l1 = str(input("location 1: "))
x1 = int(input("x1: "))
y1 = int(input("y1: "))

l2 = str(input("location 2: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

l3 = str(input("location 3: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

dis1 = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
dis2 = math.sqrt(((x1-x3)**2) + ((y1-y3)**2))
dis3 = math.sqrt(((x2-x3)**2) + ((y2-y3)**2))

if dis1 < dis2 and dis1 < dis3:
    print(l1, l2, "have the smallest distance")
elif dis2 < dis1 and dis2 < dis3:
    print(l2, l3, "have the smallest distance")
else:
    print(l1, l3, "have the smallest distance")

if dis1 > dis2 and dis1 > dis3:
    print(l1, l2, "have the largest distance")
elif dis2 > dis1 and dis2 > dis3:
    print(l2, l3, "have the largest distance")
else:
    print(l1, l3, "have the largest distance")
