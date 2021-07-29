# a, b, c ... z = 1, 2, 3 ... 26
import sys
input = sys.stdin.readline

a = list(input().strip())
len_a = len(a)
dp = [0 for i in range(len_a + 1)]
dp[0], dp[1] = 1, 1

# 처음 숫자가 0으로 시작하는 것은 10, 20으로도 만들 수 없음
if a[0] == "0":
    print(0)

else:
    for i in range(2, len_a + 1):
        # 현재 자리숫자가 0 보다 클 때 -> 이전 dp 값을 더한다
        if int(a[i - 1]) > 0:
            dp[i] += dp[i - 1]
        # 이전 자리수와 현재 자리수를 두 자리숫자로 볼 때
        num = int(a[i - 1]) + int(a[i - 2]) * 10
        if num >= 10 and num <= 26:
            dp[i] += dp[i - 2]

    print(dp[len_a] % 1000000)

    #https://jyeonnyang2.tistory.com/55