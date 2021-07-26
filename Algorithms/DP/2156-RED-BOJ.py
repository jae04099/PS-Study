#출처 [https://pacific-ocean.tistory.com/152]
n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])



'''
6 10 13 9 8 1

dp[0][0] = a[0]
dp[0][1] = dp[0][0] + a[1] or a[2]

6 10 9 8

6 10 9 1

6 13 9 1

6 13 8 1

10 13 8 1

10 9 8

2번째도 스킵

13 x (3번째부터는 스킵, 6을 더할 수 있으므로..)
'''