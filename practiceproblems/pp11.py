Problem 1 (Divisors and Prime Numbers - **)

divider = 0
sum = 0

number = int(input("enter number: "))

while divider < number:
    divider += 1
    if (number % divider) == 0:
        print(divider, end=", ")
        sum += divider
    elif divider == number:
        sum += divider
        break

if sum == 1 + number:
    print("prime number")
else:
    print("not prime")
    print("the sum is", sum)
