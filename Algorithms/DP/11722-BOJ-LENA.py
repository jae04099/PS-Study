n = int(input())
lists = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if lists[i] < lists[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# 내림차순이니 타겟보다 미만의 인덱스를 지닌 수 들이 더 커야함.
# 갯수를 세는 것 이기에 본인 포함 1로 초기화