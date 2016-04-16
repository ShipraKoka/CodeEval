import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(" ")
        F = int(line[0])
        B = int(line[1])
        n = int(line[2])
        fizzbuzz = []
        for i in range(1, n+1):
            if (i % F == 0 and i % B == 0):
                fizzbuzz.append("FB ")
            elif (i % F == 0):
                fizzbuzz.append("F ")
            elif (i % B == 0):
                fizzbuzz.append("B ")
            else:
                fizzbuzz.append(("{} ".format(str(i))))
        result = ""
        print(result.join(fizzbuzz))
            
            
            














