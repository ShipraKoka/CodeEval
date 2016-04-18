result = [2]
n = 3
while len(result) < 1000:
    for i in range(2, n):
        if (n % i) == 0 and n in result:
            result.remove(n)
            break
        elif (n % i) != 0 and n not in result:
            result.append(n)
    n += 2

answer = 0
for i in range(len(result)):
    answer += result[i]

print(answer)
  
#print(sum(result))















