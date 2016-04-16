import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(" ")
        F = int(line[0])
        B = int(line[1])
        n = int(line[2])
        fizzbuzz = ""
        for i in range(1, n+1):
            if (i % F == 0 and i % B == 0):
                fizzbuzz += "FB "
            elif (i % F == 0):
                fizzbuzz += "F "
            elif (i % B == 0):
                fizzbuzz += "B "
            else:
                fizzbuzz += ("{} ".format(str(i)))
        print(fizzbuzz)
            
            
            














