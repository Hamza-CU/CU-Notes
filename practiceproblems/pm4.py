guess = 73
close_range = 10
far_range = 20

predict = int(input("guess a number from 1-100: "))

if predict == guess:
    print("Correct!")
elif guess - far_range < predict < guess + far_range:
    if guess - close_range < predict < guess + close_range:
        print("Close but not quite correct")
    else:
        print("Nice try, but you are far away")
else:
    print("you're not very good at this")
