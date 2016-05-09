import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(",")
        
        stringA = line[0]
        stringB = line[1].strip(" ")
        
        if stringA.endswith(stringB) == True:
            print("1")
        else:
            print("0")
        




