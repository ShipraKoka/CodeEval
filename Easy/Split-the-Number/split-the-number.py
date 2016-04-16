#Python 2
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = []
        line = test.replace("\n", "").split(" ")
        if ("+" in line[1]):
            position = line[1].index("+")
            set1 = int(line[0][0:position])
            set2 = int(line[0][position:])
            print set1+set2
        else:
            position = line[1].index("-")
            set1 = int(line[0][0:position])
            set2 = int(line[0][position:])
            print set1-set2
            
            














