# n이 홀수: 0
# 이게 3 - 11 - 41 - 153인데 아래 솔루션을 제공한 글쓴이는 글로 이해하기 힘들어 직접 그리면서 이해했다고 함...

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
# 홀수이기 때문에 짝수만 계산하기 위해 2간격으로 하기 위함
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])