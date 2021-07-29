# n = int(input())
# d = [0] * (n + 1)
# p = [0] + list(map(int, input().split()))
# d[1] = p[1]
# for i in range(2, n + 1):
#     for j in range(1, i + 1):
#         if d[i] < d[i - j] + p[j]:
#             d[i] = d[i - j] + p[j]
# print(d[n])

#  최대한 돈을 많이 지불하려 함
# 인덱스: 1 2 3 4
# 가격: 1 5 6 7
# 인덱스가 곧 카드 장 수임
# 4장을 구매하기 위해 최대한 돈을 많이 지불하려면 2장이 들어 있는 5원인 것을 2개 10원에 사면 됨
# 우선 경우의 수를 구하려면 1, 2, 3, 4를 이용해서 4를 만들 수 있는 경우의 수를 구해야 할 것.
# 그 안에서 수를 비교?

# n = int(input())
# cards = list(map(int, input().split()))
# dp = [0] * n
# dp[1] = cards[1]
# dp[2] = max(dp[1] + cards[1], cards[2])
# for i in range(3, n):
#     dp[i] = max(cards[i], dp[i - 1] + dp[i - 2])
# print(dp[n - 1])

#======================================================
# dp[1] = 1
# dp[2] = 1 + 1, 2
# dp[3] = 1 + 1 + 1, 2 + 1, 3
# dp[4] = 1 + 1 + 1 + 1, 2 + 1 + 1 + 1, 2 + 2, 3 + 1, 4
n = int(input()) 
p = list(map(int, input().split())) 
dp = [0]*(n+1) 
for i in range(1, n+1): 
    for j in range(1, i+1): 
        dp[i] = max(dp[i], dp[i-j]+p[j-1]) 
print(dp[n])

#https://today-retrospect.tistory.com/47
# 1, 1, 1, 1, 1같은 경우는 이미 계산이 된 것으로 생각하면 된다는게 이해가 안감