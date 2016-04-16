import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split("|")
        scores = []
        for i in range(len(line)):
            scores.append(line[i].strip(" ").split(" "))
        n = 0
        maxValue = ""
        while n < len(scores[0]):
            compare = []
            for i in range(len(scores)):
                compare.append(int(scores[i][n]))
            n += 1
            maxValue += ("{} ".format(max(compare)))
        print(maxValue)


            
            














