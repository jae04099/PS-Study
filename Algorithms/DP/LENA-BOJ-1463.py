n = int(input())
dp = [0] * (n + 1)

# 여기서 나오는 값은 횟수가 된다.
# 1을 더하는건 계산 횟수
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    # 현재 dp[i]는 1을 뺀 것의 갯수임. 이거랑 비교해서  더 적은 수인것을 적용
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
print(dp[n])
