allthewords = str(input())
word1 = allthewords.split(' ')[0] #letters before the first space
word2 = allthewords.split(' ')[1] #letters between first space and second space
word3 = allthewords.split(' ')[2] #letters after the second space

num = int(input("enter an integer: "))

word1 = str(input("words:\n"))
word2 = str(input())
word3 = str(input())

if ((len(word1) % num) == 0):
    print(word1)
if ((len(word2) % num) == 0):
    print(word2)
if ((len(word3) % num) == 0):
    print(word3)
