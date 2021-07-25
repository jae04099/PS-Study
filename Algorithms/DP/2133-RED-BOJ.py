#그림 출처 [https://blog.naver.com/zdudmanz/222285104463]
#출처 [ https://pacific-ocean.tistory.com/208]
# n=2 일때 3 = 2 + 1
# n=4 일때 11 = 8 + 3
# n=6 일때 41 = 27 + 11 + 3
# n=8 일때 153 = 

# dp[n] = dp[n-1]
n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
print(dp[n])


'''
n = int(input())
dp = [0 for _ in range(30)]
dp[0] = 1
dp[1] = 3
dp[2] = 11
if n%2:
    print(0)
else:
    for i in range(1, n):
        dp[i] = dp[i-1] + 2**(2*i-1)
    print(dp[n-2])

n=1, dp[0] = 0
n=2, dp[1] = 2 + 1 = 3
n=3, dp[x] = 0
n=4, dp[2] = 4 + 2 + 1 = 7 // => 4 + 4+ 2 + 1 = 11 => 8 + 3

dp[n] = dp[n-1] + 3**n
'''