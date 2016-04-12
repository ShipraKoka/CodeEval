from sys import argv
script, filename = argv
file = open(filename)

for line in file:
    length = []
    words = line.replace("\n", "").split(" ")
    for word in words:
        length.append(len(word))
        if len(word) == max(length) and length.count(len(word)) == 1:
            result = word
    print(result)












