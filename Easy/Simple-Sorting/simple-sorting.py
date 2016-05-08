import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(" ")
        
        # convert from string to float
        numbers = [float(i) for i in line]
        # sort numbers
        order = sorted(numbers)
        # convert back to string
        result = [format(n, ".3f") for n in order]
        
        print(" ".join(result))



        
        













