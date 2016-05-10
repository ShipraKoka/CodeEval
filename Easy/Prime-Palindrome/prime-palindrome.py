prime = []

for num in range(3, 1000, 2):
    for divisor in range(3, num):
        if (num % divisor) == 0 and num in prime:
            prime.remove(num)
            break
        elif (num % divisor) == 0:
            break
        elif (num % divisor) != 0 and str(num) == str(num)[::-1] and num not in prime:
            prime.append(num)
            
print(prime[-1])
