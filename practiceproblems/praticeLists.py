list1 = [-12, 13, 56]
list2 = [-45, 14, 33]

def sorter(list1, list2):
    listSorted = list1 + list2
    #listSorted.sort()
    i = 0
    while i != (len(listSorted)):
        memory = 0
        value1 = int(listSorted[i])
        value2 = int(listSorted[i+1])
        if value1 > value2:
            memory = listSorted.pop(i)
            listSorted.insert(i+1, memory)
            i += 1
        else:
            i += 2

    return listSorted

listSorted = sorter(list1, list2)
print(listSorted)

________________________________________________

getInput = str(input("What Would you Like to do?: " ))
mainList = []

def measure(getMeasurement):
    if len(mainList) < 6:
        mainList.append(getMeasurement)
    else:
        mainList.remove(mainList[0])
        mainList.append(getMeasurement)
        
    return mainList

while getInput != 'q':
    if getInput == 'measure':
        getMeasurement = input("Enter a measurement, if you're done type 'a': ")
        if getMeasurement != 'a':
            getMeasurement = int(getMeasurement)
        else:
            getInput = str(input("What Would you Like to do?: " ))
        print(measure(getMeasurement))
    elif getInput == 'average':
        print("noprogram")
        
_______________________________________________________________________________________

