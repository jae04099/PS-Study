n = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(n):
    m = int(input())
    for i in range(4, m + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[m])
