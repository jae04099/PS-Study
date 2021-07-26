N = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += a[i]
   
print(max(dp))

'''
다시 보자
1  100  2  50  60   3   5   6   7   8
1, 101, 3, 53, 113, 56, 61, 67, 74, 82


dp0 = 1
dp1 = 1 + 100
dp2 = 1 + 100 + 2 (- 100 if a2 < a1) = dp1 + a2 - a1 = 3
dp3 = dp2 + a3 = 53
dp4 = dp3 + a4
dp5 = 1 + 2+ 3 (dp4 + a5  while a5 > a[i] : - a4 - a3)
'''