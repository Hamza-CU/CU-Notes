assign = float(input("Assignment Mark: "))
term = float(input("Midterm Mark: "))
exam = float(input("Exam Mark: "))

assignM = assign * 0.3
termM = term * 0.3
examM = term * 0.3
final = examM + termM + assignM

if exam >= 50 and final >= 60:
    print("pass")
else:
    print("fail")
