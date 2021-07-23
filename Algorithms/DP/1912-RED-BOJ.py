n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))

'''
10	10
-4	6
3	9	
1	10
5	15
6	21
-35	-14
12	12
21	33
-1	32

dp[0] = a[0]
dp[1] = dp[0] + a[1] or a[1]
'''