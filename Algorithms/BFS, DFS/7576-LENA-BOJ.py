# 최소일수 == bfs?
# 상자의 크기: m, n
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸
# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다
# 대각선 방향 토마토들은 영향을 주지 않음
# 토마토가 모두 익을 때 까지의 최소 날짜 출력.
# 근데 깊이 보기는 해야 할 텐데?
# 모든 토마토가 익어있는 상태 == 0 출력
# 토마토가 모두 익지는 못한다면 -1 출력
# 사분면으로 진행하는 사이클을 한번 돌 때 하루가 지난다고 치자.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 인접한 토마토를 한번 다 익히면 그게 1루프인듯.
# import collections


# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# date = 0

# def bfs(x, y):
#     queue = collections.deque
#     queue.append(matrix[x][y])
#     visited[x, y] = 1
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1


# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             dfs(i, j)
#             date += 1
# if 0 in visited:
#     print(-1)
# else:
#     print(date)
# =====================================================

# https://pacific-ocean.tistory.com/267

# from collections import deque
# m, n = map(int, input().split())
# s = []
# queue = deque()
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# for i in range(n):
#     s.append(list(map(int, input().split())))
# def bfs():
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             x = a + dx[i]
#             y = b + dy[i]
#             if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
#                 s[x][y] = s[a][b] + 1
#                 queue.append([x, y])
# for i in range(n):
#     for j in range(m):
#         if s[i][j] == 1:
#             queue.append([i, j])

# bfs()
# isTrue = False
# result = -1
# for i in s:
#     for j in i:
#         if j == 0:
#             isTrue = True
#         result = max(result, j)
# if isTrue == True:
#     print(-1)
# elif result == -1:
#     print(0)
# else:
#     print(result - 1)


# ====================================================
# https://devjin-blog.com/boj-7576-tomato/

# import sys
# from collections import deque
# r = sys.stdin.readline

# def bfs(m, n, box):
#     dx = [0, 0, 1, -1]
#     dy = [-1, 1, 0, 0]

#     days = -1

#     while ripe:
#         days += 1
#         for _ in range(len(ripe)):
#             x, y = ripe.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
#                     box[nx][ny] = box[x][y] + 1
#                     ripe.append([nx, ny])

#     for b in box:
#         if 0 in b:
#             return -1
#     return days

# # ripe: 익은 것
# m, n = map(int, r().split())
# box, ripe = [], deque()
# for i in range(n):
#     row = list(map(int, r().split()))
#     for j in range(m):
#         if row[j] == 1:
#             ripe.append([i, j])
#     box.append(row)

# print(bfs(m, n, box))

# https://jiwon-coding.tistory.com/97

# from collections import deque
# m, n = map(int, input().split())
# graph = []
# queue = deque([])
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(m):
#         # 만약 ij 좌표에 토마토가 익어있으면 queue에 넣기
#         # 하나씩 빼서 주변 익히는거같음!
#         if graph[i][j] == 1:
#             queue.append([i, j])

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs():
#     while queue:
#         # queue 안에는 익은 토마토의 좌표가 들어있음
#         x, y = queue.popleft()
#         for i in range(4):
#             a = x + dx[i]
#             b = y + dy[i]
#             # a의 동서남북을 돌 수 있고 그게 아직 익지 않았다면
#             if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
#                 # 익힐 좌표 넣기
#                 queue.append([a, b])
#                 # 날짜 더하기
#                 graph[a][b] = graph[x][y] + 1

# # bfs 돌리면 끝까지 돌 텐데
# bfs()
# answ = 0
# for i in graph:
#     for j in i:
#         # 그럼에도 0이 있으면 탈락
#         if j == 0:
#             print(-1)
#             exit(0)
#             # 다 익혔다면 최대값 출력(?) 왜지 최소아님?
#             # 가장 큰 값이 최소값이라네...
#     answ = max(answ, max(i))
# print(answ - 1)


from collections import deque
m, n = map(int, input().split())
queue = deque([])
matrix = [map(int, input().split()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a = dx[i] + x
            b = dy[i] + y
            if 0 <= a < n and 0 <= b < m and matrix[a][b] == 0:
                queue.append([a, b])
                matrix[a][b] = matrix[x][y] + 1

bfs()
ans = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    ans = max(ans, max(i))
print(ans - 1)








