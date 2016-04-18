import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n")
        rep = ""
        for l in line:
            if not rep or l != rep[0]:
                rep += l
            else:
                break
        print(len(rep))
            
        













