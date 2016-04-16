#Python 2
import sys

with open(sys.argv[1], 'r') as test_cases:
    words = []
    for test in test_cases:
        words = test.replace("\n", "").split(" ")
        line = [word[0].upper() + word[1:] for word in words]
        newLine = ""
        for i in line:
            newLine += i+" "
        print newLine
            














