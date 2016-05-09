import sys

line=[]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line.append(test.strip("\n"))
        
    num = int(line.pop(0))
    #sort strings by length in descending order
    line.sort(key = len, reverse=True)
    
    i = 0
    while i < num:
        print(line[i])
        i += 1
        
        




