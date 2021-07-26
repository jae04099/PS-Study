#출처 [https://pacific-ocean.tistory.com/66]

n = int(input())
d = [0] * (n + 1)
p = [0] + list(map(int, input().split()))
d[1] = p[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if d[i] < d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[n])


'''

10
1 1 2 3 5 8 13 21 34 55

dp[0] = 1 * 10
dp[1] = max(dp[0], a[1] * 5)
dp[2] = max(dp[1], a[2] * 3 + a[0])
dp[3] = max(dp[2], a[3] * 2 + a[0]*2 or a[1])
'''