# 1 = 1**2
# 2 = 1**2 + 1**2
# 3 = 1**2 + 1**2 + 1**2
# 4 = 2**2
# 5 = 2**2 + 1**2
# 6 = 2**2 + 1**2 + 1**2
# 7 = 2**2 + 1**2 + 1**2 + 1**2
# 8 = 2**2 + 2**2
# 9 = 3**2
# 10 = 3**2 + 1**2

# 자체가 제곱수로 끝날 수 있으면 1로 리셋
# 그 다음 수는 아래에서 구해둔 횟수 더해서 결과봄
# (타겟 수 - 가장 가까운 제곱수) 에서 구해 둔 갯수 + 가장 가까운 제곱수
# import math
# import sys

# input = sys.stdin

# n = int(input())
# mult = []
# dp = [0] * 100001
# dp[0] = 1
# dp[1] = 2
# dp[2] = 3
# dp[3] = 1
# for i in range(4, n):
#     if math.sqrt(i) == int(math.sqrt(n)):
#         dp[i] = 1
#         mult.append(i)
#     else:
#         dp[i] = dp[i - mult[-1]] + 1
# print(dp[n - 1])

# 답은 맞는데 런타임 에러 뜸 아마 mult를 계속 append해서?

n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []  # 
    for j in square:
        # 이 방법으로 제일 가까운 제곱수를 찾을 수 있다
        # i 보다 작은 수들 중 제곱수인 것 중
        if j > i:
            break
        s.append(dp[i - j])
        # 제일 작은 수가 되는 것의
    dp[i] = min(s) + 1
print(dp[n])