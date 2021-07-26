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

n = int(input())
cards = list(map(int, input().split()))
dp = [0] * n
for i in range(n):

