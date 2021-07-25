# n = int(input())
# lists = list(map(int, input().split())) # 리스트에 변화를 줄 수 없음
# dp = [i for i in lists] # 리스트에 변화를 줄 수 있음
# for i in range(1, n):
#     dp[i] = max(dp[i - 1], lists[i - 1] + dp[i] )
# print(max(dp))

# 예제 2 통과가 안됨...

n = int(input())
a = list(map(int, input().split())) # 10 -4 3 1 5 6 -35 12 21 -1
sum = [a[0]]    # 10
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))    # 연속해서 더하는것, 그 다음수 중 더 큰 것
print(max(sum))

# 