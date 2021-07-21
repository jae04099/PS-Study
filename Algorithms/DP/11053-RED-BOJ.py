n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))


# N = int(input())
# a = list(map(int, input().split()))

# dp = [min(a)]

# for i in range(a.index(min(a)), N):
#     dp.append(max(a[i], dp[-1]))

# print(len(set(dp)))

'''
10
d[0] = min(a)

10 20
d[1] = max(a[1], d[0])

10 20 10
d[2] = a[2] if d[1] < a[2] else d[1]

10 20 10 30
d[3] = 30

10 20 10 30 20
d[4] = 30

10 20 10 30 20 506
d[5] = 50
'''