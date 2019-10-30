file = input("Enter a file name: ")
f = open(file, "r")

totalSum = 0
numOfGrades = 0
classAverage = 0
passes = 0
fails = 0
highestMark = 0
lowestMark = 100

nameF = f.readline().strip()

while nameF != "":
    nameL = f.readline().strip()
    studentNumber = f.readline().strip()

    assignmentGrade = int(f.readline().strip()) * 0.25
    midtermGrade = int(f.readline().strip()) * 0.25
    examGrade = int(f.readline().strip()) * 0.5

    finalGrade = assignmentGrade + midtermGrade + examGrade

    totalSum += finalGrade
    numOfGrades += 1

    if finalGrade >= 50 and examGrade >= 25:
        passes += 1
    else:
        fails += 1

    if finalGrade > highestMark:
        highestMark = finalGrade
        smartestStudent = nameF + nameL
    if finalGrade < lowestMark:
        lowestMark = finalGrade
        dumbestStudent = nameF + nameL

    nameF = f.readline().strip()

average = (totalSum / numOfGrades)

print("The class average was: ", average)
print("The number of people who passed:", passes)
print("The number of people who failed:", fails)
print("The highest mark belonged to", smartestStudent, "who got a", highestMark)
print("The lowest mark belonged to", dumbestStudent, "who got a", lowestMark)
