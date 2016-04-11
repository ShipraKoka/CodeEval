from sys import argv
script, filename = argv
file = open(filename)

def unique(numbers):
    i = 0
    newList = []
    for num in numbers:
        if numbers[i] not in newList:
            newList.append(numbers[i])
        i+=1
    print(str(newList).strip("[]").replace(" ", ""))
    #print(str(newList).strip("[]").translate(None, " "))

for line in file:
    numbers = [int(s) for s in line.split(",")]
    unique(numbers)







