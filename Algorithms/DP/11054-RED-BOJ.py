#출처 [https://pacific-ocean.tistory.com/158]
n = int(input())
a = list(map(int, input().split()))
dpp = [0 for i in range(n)]
dpm = [0 for i in range(n)]
dpb = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dpb[i] = dpp[i] + dpm[i] - 1
print(max(dpb))

'''
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

summit = a[0]
for i in range(n):
    if a[i] > summit:
        summit = a[i]
        for j in range(i):
            print(j)
    elif a[i] < summit:
        for j in range(i):
            print(j)

    dp[i] += 1

print(dp)


1 5 2 1 4 3 4 5 2 1
1 2 3 4 3 4 4

dp[0] = 1 , summit = 1
dp[1] = 1 + 1 if summit < a[1] and a[0] < a[1], summit = a[1] or summit > a[1] summit =5
dp[2] = 3
summit = 5
a[0] < a[2] True => dp[2] = dp[0]
a[1] < a[2] False => a[2] > summit False => dp[2] = dp[1]
dp[3] = 3 + 1..
dp[4] =
a[4] = 4
summit = 5
a[0] < a[4] True => dp[4] = dp[0]
a[1] < a[4] False => a[4] > summit False => dp[4] = dp[1]
a[2] < a[4] True 
a[3] < a[4] True
'''