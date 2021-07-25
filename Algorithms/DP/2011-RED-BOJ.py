#출처 [https://it-sunny-333.tistory.com/78]
a = list(map(int, list(input())))
l = len(a)

# dp[i] : i번째 수 단계에서 암호 코드의 개수
dp = [0] * (l+1)

if a[0] == 0: # 암호 만들 수 없는 경우
    print(0)
else :
    a = [0] + a # 인덱싱을 위해 추가한 0
    dp[0] = 1
    dp[1] = 1 # 첫번째 수로 이뤄진 암호코드는 1개이다.

    for i in range(2, l+1):
        cur = a[i] # 한 자리
        cur2 = a[i-1] * 10 + a[i] # 두 자리
        print(cur, cur2)
        if cur >= 1 and cur <= 9:
            dp[i] += dp[i-1]
        if cur2 >= 10 and cur2 <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    print(dp[l])

'''
n = str(input())

print(n[0:2], n[2:4])
for i in range(len(n)):
    print(i)

25114

띄어쓰기
1 :
25 114 x

2:
25 11 4	a[0:2], a[2:4], a[4:]
25 1 14	a[0:2], a[2:3], a[3:]
2 51 14 x a[0:1], a[1:3], a[3:]
2 5 114 x

3:
25 1 1 4	a[0:2] a[2:3] a[3:4] a[4:]
2 51 1 14 x
2 5 11 14
'''