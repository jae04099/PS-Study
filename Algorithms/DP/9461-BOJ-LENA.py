n = int(input())
dp = [0] * 101
dp[0], dp[1], dp[2] = 1, 1, 1
for i in range(n):
    test = int(input())
    for j in range(3, test):
        dp[j] = dp[j - 2] + dp[j - 3]
    print(dp[test - 1])

