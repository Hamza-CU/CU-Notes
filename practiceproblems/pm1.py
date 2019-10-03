#practice midterm 1

response1 = str(input("is there a test tomorrow?: "))
response2 = str(input("Is it past 12 o'clock?: "))

if response1 == "yes":
    print("study")
elif response1 == "no" and response2 == "yes":
    print("sleep")
else:
    print("game")
