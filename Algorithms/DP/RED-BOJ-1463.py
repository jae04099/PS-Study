#[출처] https://infinitt.tistory.com/247
#점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )

n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])



#처음 생각한것
# n = map(int, input().split())
# n = int(input().split()[0])
#3으로 나눈 나머지가 2이면 2로나누고, 최대한 3으로 나눌 수 있게..

# n = 100

# def three(n):
#     count = 0

#     while n > 1:
#         if int(n % 3) == 2:
#             if int(n % 2) == 0:
#                 n = int(n / 2)
#             else:
#                 n -= 1
#         elif int(n % 3) == 1:
#             n -= 1
#         else:
#             n = int(n / 3)
#         count += 1
#     return count

# def two(n):
#     count = 0
#     while n > 1:
#         if int(n % 3) == 0:
#             n = int(n / 3)
#         elif int(n % 2) == 0:
#             n = int(n / 2)
#         else:
#             n -= 1
#         count += 1
#     return count

# print(min(three(n), two(n)))
        