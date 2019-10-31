filename = (input("Whatfile?: "))
f = open(filename, "r")

def largestvolume(filename):
    length = int(f.readline().strip())
    width = int(f.readline().strip())
    height = int(f.readline().strip())
    largestvolume = 0
    while length != "":
        volume = length * width * height
        if largestvolume < volume:
            largestvolume = volume
        
        length = int(f.readline().strip())
        width = int(f.readline().strip())
        height = int(f.readline().strip())
        
    return largestvolume

print(largestvolume(filename))
