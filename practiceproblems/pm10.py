N = int(input("Enter an Integer: "))

def sumdivisors(N):
    sumOfDivisors = 0
    divisor = N
    while divisor > 0 :
        if (N % divisor) == 0:
            sumOfDivisors += divisor
        divisor -= 1
    return sumOfDivisors

print(sumdivisors(N))
