#출처 [https://pacific-ocean.tistory.com/205]

n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])


'''
import math
n = int(input())
count = 0

while n > 0:
    if n > 2:
        for i in range(1, int(math.sqrt(n))):
            if n <= i**2:
                n = n - int(n**0.5)**2
            else:
                r = math.sqrt(n - i**2)
                if round(r, 3) == r:
                    n = n - int(i**0.5)**2
                else:
                    n = n - int(n**0.5)**2
    else:
        n = n - int(n**0.5)**2
    count += 1

print(count)
'''
'''
n = int(input())
count = 0

while n > 0:
    n = n - int(n**0.5)**2
    print(n)
    count += 1

print(count)
11
dp[0] = 11 ** 0.5, n = 11 - int(11**0.5)**2 = 2
dp[1] = dp[0]**0.5, n = 2 - int(2**0.5)**2 = 1
dp[2] = dp[1]**0.5, n = 1 - .. = 0


52
52 - 49 = 3
3 - 2 = 1
1 - 1 = 0
count = 4

52 - 36 = 16
16 - 16 = 0
count = 2
'''
