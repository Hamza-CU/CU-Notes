totalSum = 0
numOfGrades = 0
classAverage = 0
passes = 0
fails = 0
highestMark = 0
lowestMark = 0

file = input("Enter a file name: ")
f = open(file, "r")

i = 0
while i == 0:
    nameF = f.readline().strip()

    if nameF == " ":
        f.close()
        break

    nameL = f.readline().strip()
    studentNumber = f.readline().strip()

    assignmentGrade = int(f.readline().strip())
    midtermGrade = int(f.readline().strip())
    examGrade = int(f.readline().strip())

    finalGrade = (assignmentGrade/4) + (midtermGrade/4) + (examGrade/2)

    totalSum += finalGrade
    numOfGrades += 1

    if finalGrade >= 50 and examGrade >= 50:
        passes += 1
    else:
        fails += 1

    if finalGrade > highestMark:
        highestMark = finalGrade
        smartestStudent = nameF + nameL
    if finalGrade < lowestMark:
        lowestMark = finalGrade
        dumbestStudent = nameF + nameL

average = (totalSum / numOfGrades)

print("The class average was: ", average)
print("The number of people who passed:", passes)
print("The number of people who failed:", fails)
print("The highest mark belonged to", smartestStudent, "who got a", highestMark)
print("The lowest mark belonged to", dumbestStudent, "who got a", lowestMark)
