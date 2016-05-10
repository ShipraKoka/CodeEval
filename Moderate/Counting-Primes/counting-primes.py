import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split(",")
        N = int(line[0])
        M = int(line[1])
        primes = []
        
        for num in range(N, M+1):
            if num == 1:
                pass
            elif num == 2:
                primes.append(num)
            for divisor in range(2, num):
                if (num % divisor) == 0 and num in primes:
                    primes.remove(num)
                    break
                elif (num % divisor) == 0:
                    break
                elif (num % divisor) !=0 and num not in primes:
                    primes.append(num)
                    
        print(len(primes))
