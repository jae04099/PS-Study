#RETRY!!!
#[출처] https://pacific-ocean.tistory.com/151
n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)

#n = 3
# n = int(input())
# dp = [9, 17]
# dp.extend(0 for _ in range(2, n+1))

# for i in range(2, len(dp)):
#     dp[i] = (dp[i-1]-1)*2

# print(dp[n-1]%1000000000)

'''
dp[1] = 9
dp[2] = 17
dp[3] = 32
dp[n] = (dp[n-1]-1) * 2

101
121
123

210
212
232
234

321
323
343
345

432
434
454
456

543
545
565
567

654
656
676
678

765
767
787
789

876
878
898

987
989


'''