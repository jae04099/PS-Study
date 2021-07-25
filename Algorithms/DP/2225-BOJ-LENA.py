# 0부터 20까지의 정수 중 2개를 더해서 합이 20이 되는 것의 갯수?
n, k = map(int, input().split())
s = [[0] * 201 for i in range(201)]
for i in range(201):
    s[i][1] = 1
for i in range(1, 201):
    for j in range(201):
        for l in range(j + 1):
            s[j][i] += s[l][i - 1]
print(s[n][k] % 1000000000)