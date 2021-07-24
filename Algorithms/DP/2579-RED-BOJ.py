#[출처] https://pacific-ocean.tistory.com/149
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])

# n = int(input())
# a = []
# dp = [0 for _ in range(n)]
# for i in range(n):
#     a.append(int(input()))

# dp[0] = a[0]
# dp[1] = a[0] + a[1]
# for i in range(2, n):
#     if i == n:
#         dp[i] = dp[i-1] + a[i]
#     else:
#         dp[i] = max(dp[i-1], dp[i-2] + a[i])

# print(dp)

'''
dp[i] = max(dp[i-1], dp[i-2] + a[i])
dp[n] = dp[n-1] + a[n]

20	dp[5] = dp[4] + a[5]
10	dp[4] = max(dp[3], dp[2] + a[4])
25	dp[3] = max(dp[2], dp[1] + a[3])
15	dp[2] = max(dp[1], dp[0] + a[2])
20	dp[1] = dp[0] + a[1]
10	dp[0] = a[0]
'''