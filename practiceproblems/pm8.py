filename =  input("Enter filename: ")

def getAverageGrade(filename):
    f = open(filename, "r")

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
    f = open(filename, "r")

    highestMark = 0
    #bestStudent = ""
    sid = ""
    studentID = f.readline().strip()
    while studentID != "":
        studentGrade = int(f.readline().strip())
        #print(studentID)
        if studentGrade > highestMark:
            sid = studentID
        studentID = f.readline().strip()
    return sid

print("the average is", getAverageGrade(filename), "%. The best student is", getBestStudent(filename))
