# (1, 1)에서 출발해 (n, m) 의 위치로....최소 칸 수
# from collections import deque

# m, n = map(int, input().split())
# matrix = [list(input()) for _ in range(m)]

# def bfs():

# str = '101111'
# lists = list(str)
# print(lists)

# n, m = map(int, input().split())
# s = []
# queue = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# for i in range(n):
#     s.append(list(input()))
# queue = [[0, 0]]
# s[0][0] = 1
# while queue:
#     a, b = queue[0][0], queue[0][1]

# from sys import stdin
# from collections import deque
# n, m = map(int, stdin.readline().split())
# # 받은 경로 배열
# matrix = [stdin.readline().rstrip() for _ in range(n)]
# # 방문 체크용 배열
# visited = [[0] * m for _ in range(n)]
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# # 0, 0부터 ㄱㄱ하기
# queue = deque([(0, 0)])
# visited[0][0] = 1

# while queue:
#     x, y = queue.popleft()

#     if x == n - 1 and y == m - 1:
#         print(visited[x][y])
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
#                 visited[nx][ny] == visited[x][y] + 1
#                 queue.append((nx, ny))


from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
q = deque()
check = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
 
q.append((0,0))
check[0][0] = True
dist[0][0] = 1
 
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == False and a[nx][ny] == 1:
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True
print(dist[n-1][m-1])