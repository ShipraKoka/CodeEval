import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n")
        print("{0:b}".format(int(line)))
