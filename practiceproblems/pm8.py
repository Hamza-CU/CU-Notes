filename =  input("Enter filename: ")
f = open(filename, "r")

def getAverageGrade(filename):
    totSum = 0
    totNums = 0
    studentID = f.readline().strip()
    studentGrade = f.readline().strip()
    while studentID != "":
        totSum += int(studentGrade)
        totNums += 1
        studentID = f.readline().strip()
        studentGrade = f.readline().strip()

    average = (totSum / totNums)
    return average

def getBestStudent(filename):
    highestMark = 0
    studentID = f.readline().strip()
    studentGrade = f.readline().strip()
    bestStudent = ""
    while studentID != "":
        if studentGrade > highestMark:
            bestStudent = studentID
        studentID = f.readline().strip()
        studentGrade = f.readline().strip()
    return bestStudent


print("the average is", getAverageGrade(filename), "%. The best student is", getBestStudent(filename))
