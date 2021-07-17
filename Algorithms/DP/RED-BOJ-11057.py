dp = [
    [1 for _ in range(10)],
    [i for i in range(10, 0, -1)]
    ]
dp.extend([[0 for _ in range(10)] for _ in range(998)])

n = int(input())
for j in range(2, n):
    for i in range(10):
        if i == 0:
            dp[j][0] = sum(dp[j-1])
        else:
            dp[j][i] = dp[j][i-1] - dp[j-1][i-1]

print(sum(dp[n - 1])%10007)

'''
n \ 0 1 2 3 4 5 6 7 8 9 (앞자리)
1	1 1 1 1 1 1 1 1 1 1
2  10 9 8 7 6 5 4 3 2 1
3  55 45 36 ...		  11

dp[3][0] = sum(dp[2]) = 55
dp[3][1] = 65 - dp[2][0] = 55
dp[3][2] = 55 - dp[2][1] = 46


000
~
009
011
~
019
022
~
029
...
099
=> 10 + 55 = 65

65 - 10 = 55
55 - 9 = 46
46 - 8 = 38
38 - 7 = 31
31 - 6 = 25
25 - 5 = 20
20 - 4 = 16
16 - 3 = 13
13 - 2 = 11


'''