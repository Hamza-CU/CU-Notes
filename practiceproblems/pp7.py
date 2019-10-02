#Problem 2 (Leap Years - **)

year = int(input("please input a year and I will check if its a leap year\n"))

check1 = (year % 100)
check2 = (year % 400)
check3 = (year % 4)

if check1 == 0:
    if check2 == 0:
        print("leap-year")
    else:
        print("not a leap-year")
else:
    if check3 == 0:
        print("leap-year")
    else:
        print("not a leap year")
