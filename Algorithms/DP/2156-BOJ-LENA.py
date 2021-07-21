# 연속으로 놓여 있는 3잔을 모두 마실 수는 없음
# 포도주 잔을 마신 후 잔은 원래 위치에 다시 놓아야 함(?)

# n = int(input())
# lists = [int(input()) for _ in range(n)]
# dp = [0] * n
# result = 0
# for i in range(3, n):
#     dp[i] += max(lists[i - 1] + lists[i - 3], lists[i - 2] + lists[i - 3])

# print(dp)

n = int(input())
lists = [int(input()) for _ in range(n)]
dp = [0] * n
result = 0
i = 3
while i <= n:
    dp[i] += max(lists[i - 1] + lists[i - 3], lists[i - 2] + lists[i - 3])


print(dp)

# https://www.acmicpc.net/board/view/60664
# 이해 필요