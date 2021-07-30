# n = 사람의 수, lists = 인출에 걸리는 시간
# 인출하는데 필요한 시간의 최솟값은 곧 오름차순이어야 하지 않을까?
# 그냥 소팅하고 dp씀

n = int(input())
lists = sorted(list(map(int, input().split())))
dp = [0] * n
dp[0] = lists[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + lists[i]
print(sum(dp))
