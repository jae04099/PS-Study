# n = int(input())
# lists = (list(map(int, input().split())))
# dp = [0] * n

# for i in range(n):
#     for j in range(i):
#         if lists[i] > lists[j]:
#             dp[i] = max(dp[i], dp[j] + lists[i])
# print(dp)

# lists = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
# dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = int(input())
lists = list(map(int, input().split()))
dp =  [i for i in lists]

for i in range(n):
    for j in range(i):
        if lists[i] > lists[j]:
            dp[i] = max(dp[i], dp[j]+lists[i])
print(max(dp))

# 횟수는 1로 초기화, 합은 그냥 받아온 값과 같은 배열로 초기화