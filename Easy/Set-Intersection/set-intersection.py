import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(";")
        firstList = line[0].strip(" ").split(",")
        secondList = line[1].split(",")
        intersection = [x for x in firstList if x in secondList]
        print(",".join(intersection))
