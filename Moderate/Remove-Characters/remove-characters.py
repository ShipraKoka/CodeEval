import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.split(",")
        words = line[0].lstrip(" ")
        letters = line[1].lstrip(" ")

        for i in letters:
            words = words.replace(i, "")
        print words
