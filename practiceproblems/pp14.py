totSum = 0
totInputs = 0
average = 0
totPosNums = 0
totNegNums = 0
highestNum = 0
lowestNum = 0
i = 0

file = input("Enter a file name: ")
f = open(file, "r")

while i == 0:
    number = f.readline().strip()
    if number == "":
        f.close()
        break
    number = int(number)
    totSum = number + totSum
    totInputs = totInputs + 1
    average = (totSum / totInputs)
    if number > 0:
        totPosNums = totPosNums + 1
    elif number < 0:
        totNegNums = totNegNums + 1
    else:
        totNegNums = totNegNums + 0
        totPosNums = totPosNums + 0

    if number > highestNum:
        highestNum = number
    if number < lowestNum:
        lowestNum = number

print(totSum)
print(totNegNums)
print(totPosNums)
print(average)
print(highestNum)
print(lowestNum)
