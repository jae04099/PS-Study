# 0부터 20까지의 정수 중 2개를 더해서 합이 20이 되는 것의 갯수?
n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])