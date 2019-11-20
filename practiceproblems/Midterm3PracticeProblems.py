userArgument = input("input a string: ")

def letterCount(userArgument):
    letterDictionary = {}
    organized = list(userArgument)

    for item in organized:
        if (item in letterDictionary):
            letterDictionary[item] += 1
        else:
            letterDictionary[item] = 1
    
    return letterDictionary

print(letterCount(userArgument))

_________________________________________

filename = input("What file would you like to read from?: ")
keyword = input("What character(s) would you like to search for?: ")

def search_employees(filename, keyword):
    fi = open(filename, "r")
    f = fi.readline().strip()
    
    data = []
    
    while f != '':
        empNumber = f.split(',')[0]
        empName = f.split(',')[1]
        empPay = f.split(',')[2]
        data.append(empName)
        f = fi.readline().strip()
    
    print(data)
    keywordSearch = []
    for i in range(0, len(data)):
        if keyword.lower() in data[i].lower():
            keywordSearch.append(i)

    return keywordSearch

def analyze_pay(filename):
    fi =  open(filename, "r")
    f = fi.readline().strip()

    paySum = 0
    payments = 0 
    largestPay = 0
    smallestPay = 1000000000000000000000000000
    
    while f != '':
        empNumber = int(f.split(',')[0])
        empName = f.split(',')[1]
        empPay = int(f.split(',')[2])

        paySum += empPay
        payments += 1
        if empPay > largestPay:
            largestPay = empPay
        
        if empPay < smallestPay:
            smallestPay = empPay

        f = fi.readline().strip()

    averagePay = (paySum / payments)

    outputs = [averagePay, smallestPay, largestPay]

    return outputs


print(search_employees(filename, keyword))
print(analyze_pay(filename))
