# n = int(input())
# lists = [int(input()) for _ in range(n)]
# dp = [0] * 1001
# dp[0] = lists[0]
# dp[1] = lists[1]

# for i in range(2, n + 1):
#     if dp[i - 2] < dp[i - 1]

# 자기 자신보다 작은 수를 구해야 하므로, 일차원 배열이지만 이중for문을 사용한다.

# n = int(input())
# lists = [int(input()) for _ in range(n)]
# dp = [0] * 1001

# dp 문제라는걸 알고 나면 스테레오타입으로 정신을 못차림
# 첫번째 숫자와 두번째 숫자는 구해 놔야 문제를 풀 수 있을것이다 등...

n = int(input())
lists = list(map(int, input().split()))
# lists = [int(input()) for _ in range(n)]
# 위 처럼 적으면 런타임에러남
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if lists[j] < lists[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))