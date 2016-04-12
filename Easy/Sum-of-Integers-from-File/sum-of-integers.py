from sys import argv
script, filename = argv
file = open(filename)

total = 0
for line in file:
    total += int(line)
print(total)












