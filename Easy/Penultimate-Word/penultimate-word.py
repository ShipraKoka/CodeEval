import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.split(" ")
        print(line[-2])
