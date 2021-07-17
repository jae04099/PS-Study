#예상 점화식 dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

test = int(input())

dp = [1, 2, 4]
dp.extend(0 for _ in range(7))

for i in range(3, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(test):
    n = int(input())
    print(dp[n-1])


'''
1
=> 0

2
=> 2

3
1+1+1
1+2
2+1
=>3

4
=>7

5
1+1+1+1+1 => 1
1+1+1+2 => 4
1+2+2 => 3
1+1+3 => 3
1+4 => 2
2+3 =>2
=> 15

dp[1] = 0
dp[2] = 2
dp[3] = 3
dp[4] = 7
dp[5] = 15

'''