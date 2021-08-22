# 작은 직사각형의 합은 그 속에 있는 수의 합
# 세 개의 작은 직사각형의 합의 곱의 최댓값
# 직사각형 조건: n*m이 돼야 함

# n, m = map(int, input().split())
# numList = [(int(i) for i in str(input())) for _ in range(n)]
# matrix = [[0] * m for _ in range(n)]
# max_res = 0
# fir, sec, thr = [0][0]
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# while 0 in matrix:
#     dp


#========================================================
# https://suri78.tistory.com/151
# ?

import sys
 
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans = 0
 
# |||
for i in range(1, m-1):
    for j in range(i+1, m):
        s1 = sum([table[a][b] for a in range(n) for b in range(i)])
        s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)
 
# ||
# --
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)
 
# --
# ||
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)
 
# =|
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)
 
# |=
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j)])
        ans = max(ans, s1*s2*s3)
 
# -
# -
# -
for i in range(1, n-1):
    for j in range(i+1, n):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)
 
print(ans)


# https://sdesigner.tistory.com/m/52
n, m = map(int, input().split())

# 입력받은 전체 직사각형을 저장하기 위한 리스트(편리한 인덱싱을 위해 행 삽입)
rectangle_input = [[0 for _ in range(m + 1)]]


for _ in range(n):
    # 라인별로 읽고 rectangle_input에 저장(편리한 인덱싱을 위해 [0] 삽입)
    line_input = [0] + list(map(int, list(input())))
    rectangle_input.append(line_input)


# 답은 최댓값을 출력해야 하므로, 0으로 시작
ans = 0

# 합을 저장할 리스트
s = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 리스트 s는 입력받은 직사각형의 1,1부터 영역 내 모든 수의 합을 저장
for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + rectangle_input[row][col]


def sum_cal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]


# 첫 번째 경우: 전체 직사각형을 세로로만 분할한 경우
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3


# 두 번째 경우: 전체 직사각형을 가로로만 분할한 경우
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, j, m)
        r3 = sum_cal(j+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 세 번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
for i in range(1, m):
    for j in range(1, n):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, j, m)
        r3 = sum_cal(j+1, i+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 네 번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 다섯번 째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(i+1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

# 여섯번 째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(1, j+1, i, m)
        r3 = sum_cal(i+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

print(ans)