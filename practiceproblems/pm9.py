filename =  input("what file?: ")
f = open(filename, "r")

def analyze(filename):
    evenLength = 0
    highestLength = 0
    line = int(f.readline().strip())
    while line != "":
        if line % 2 == 0:
            evenLength += 1
        else:
            highestLength = evenLength
            evenLength = 0
        line = f.readline().strip()

    return highestLength

print(analyze(filename))
