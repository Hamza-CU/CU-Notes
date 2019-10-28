#Problem 5 (Tracking Numbers - **)

totSum = 0
totNumCount = 0
posNumCount = 0
negNumCount = 0
average = 0
largest = 0
smallest = 0

i = 0

f = open('numbertest1.txt', 'r')

number = int(f.readline().strip())

while number != '':

    print(number)
    number = int(f.readline().strip())
    int(number)
    totSum = totSum + number
    totNumCount = totNumCount + 1
    average = (totSum/totNumCount)
    if number > 0:
        posNumCount += 1
    elif number < 0:
        negNumCount += 1

print("Positive Numbers:", posNumCount)
print("Negative Numbers:", negNumCount)
print("Largest Number:", )
print("Smallest Number:", )
