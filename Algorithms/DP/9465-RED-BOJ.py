#출처 [https://m.blog.naver.com/occidere/220786307316]
#d[0][i] = Max(d[1][i - 1], d[1][i - 2]) + a[0][i];
#d[1][i] = Max(d[0][i - 1], d[0][i - 2]) + a[1][i];

#출처2 [https://pacific-ocean.tistory.com/197]
t = int(input())
for i in range(t):
    s = []
    n = int(input())
    for k in range(2):
        s.append(list(map(int, input().split())))
    s[0][1] += s[1][0]
    s[1][1] += s[0][0]
    for j in range(2, n):
        s[0][j] += max(s[1][j - 1], s[1][j - 2])
        s[1][j] += max(s[0][j - 1], s[0][j - 2])
    print(max(s[0][n - 1], s[1][n - 1]))
'''
T = 1
n = 5
a = [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]

dp = [0, 0]

if n == 1:
    print(max(a[0][0], a[1][0]))

elif n == 2:
    print(max(a[0][0] + a[1][1], a[1][0] + a[0][1]))
else:
    for i in range(2):
        for j in range(n):
            if i == 0:
                if j == 0:
                    dp[0] =  max(a[1][j] + a[1][j+1], a[1][j] + a[1][j+2])
                if j+2 < n:
                    dp[0] = max(dp[0] + a[1][j+1], dp[0] + a[1][j+2])
                elif j+1 < n:
                    dp[0] = dp[0] + a[i+1][j+1]
            if i == 1:
                if j == 0:
                    dp[1] = max(a[i-1][j] + a[i-1][j+1], a[i-1][j] + a[i-1][j+2])
                if j+2 < n:
                    dp[1] = max(dp[1] + a[i+1][j+1], dp[0] + a[i+1][j+2])
                elif j+1 < n:
                    dp[1] = dp[1] + a[i+1][j+1]


a[0][0]
=> a[1][1] or a[1][2]

max(a[0][0] + a[1][1], a[0][0] + a[1][2])
'''