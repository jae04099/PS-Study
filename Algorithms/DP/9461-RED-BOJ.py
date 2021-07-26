T = int(input())
dp = [0 for _ in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i-2] + dp[i-3]

for i in range(T):
    n = int(input())
    print(dp[n-1])



'''
1, 1, 1, 2, 2, 3, 4, 5, 7, 9
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2 = dp[1] + dp[0]
dp[4] = 2 = dp[2] + dp[1]
dp[5] = 3 = dp[3] + dp[2]
dp[6] = 4
dp[7] = 5
dp[8] = 7
dp[9] = 9 = dp[7] + dp[6]
'''