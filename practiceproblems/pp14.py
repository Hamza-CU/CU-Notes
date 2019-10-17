#Problem 5 (Tracking Numbers - **)

i = 0
totSum = 0
totNumCount = 0
posNumCount = 0
negNumCount = 0
average = 0
largest = 0
smallest = 0

while i == 0:
    response = int(input("Enter a number: "))
    if response == int:
        int(response)
        totSum += response
        totNumCount += 1
        average = (totSum/totNumCount)
        if response > 0:
            posNumCount += 1
        elif response < 0:
            negNumCount += 1
    else:
        print("Positive Numbers:", posNumCount)
        print("Negative Numbers:", negNumCount)
        print("Average of Numbers:", average)
        print("Largest Number:", )
        print("Smallest Number:", )
        break
