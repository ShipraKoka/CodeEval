import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n")
        word = list(line)

        for i in word:
            if word.count(i) == 1:
                print(i)
                break
