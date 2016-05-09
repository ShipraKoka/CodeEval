import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(",")
        words = [word for word in line if word.isdigit() == False]
        digits = [digit for digit in line if digit.isdigit() == True]
        
        if not words:
            print(",".join(digits))
        elif not digits:
            print(",".join(words))
        else:
            print(",".join(words) + "|" + ",".join(digits))
