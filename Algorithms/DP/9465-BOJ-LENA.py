# 이동이 가능 한 경우, 가능 하지 않은 경우 = 0보다 같거나 크고 아닌경우
# 이미 이동을 한 경우 = p
# 이미 제거 된 경우 = -1
# 근데 왜 dp? 이동하면서 수를 점진적으로 max인걸로 바꿔치기 하나?
# 대각선 위의 값 혹은 그 다음 값 중에 큰 것을 골라서 바꿔치기?


# n = int(input())
# for i in range(n):
#     row = int(input())
#     stickers = [list(map(int, input().split())) for i in range(2)]
#     start = max(stickers[0][0], stickers[1][0])
#     for j in range(2):
#         for k in range(row):
#             if j == 0:
#                 stickers[j][k] = max(stickers[j + 1][k + 1], stickers[j + 1][k + 2])
#     print(stickers)

#----------------------------------------------------------------------------------------

t = int(input())
for i in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    for j in range(2, n):
        stickers[0][j] += max(stickers[1][j - 1], stickers[1][j - 2])
        stickers[1][j] += max(stickers[0][j - 1], stickers[0][j - 2])
    print(max(stickers[0][n - 1], stickers[1][n - 1]))

# 바텀업인거 제발 헷갈리지 말기
# 목표가 제일 마지막 수 라면 이전의 수 부터 구해야 하므로 -를 씀