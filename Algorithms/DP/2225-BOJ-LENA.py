# 0부터 20까지의 정수 중 2개를 더해서 합이 20이 되는 것의 갯수?
# n = 합, k = 정수의 갯수
import sys
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[k][n])

# 표 만들어봐야 암