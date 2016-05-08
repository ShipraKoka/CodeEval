import sys, itertools

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n")
        sortedString = "".join(sorted(line))
        result = list(map("".join, itertools.permutations(sortedString)))
        print(",".join(result))




        
        













