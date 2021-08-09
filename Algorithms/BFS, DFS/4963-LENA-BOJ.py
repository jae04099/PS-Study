# w = 너비 h = 높이
# 최대한 깊이 들어가서 한 사이클이 되면  +1
# 1은 땅, 0은 바다
# 대각선 따지려면 
# dx, dy = [1, -1, 1, -1], [1, -1, -1, 1]
# 대각선을 먼저 따져야 하나? 

# w, h = 1, 1
# dx = [1, 1, -1, -1, 1, -1, 0, 0]
# dy = [0, 1, 0, 1, -1, -1, 1, -1]

# def dfs(x, y):
#     visited[x][y] = 1
#     for i in range(8):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < h and 0 <= ny < w:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
#                 dfs(nx, ny)         

# while w != 0 and h != 0:
#     res = 0
#     w, h = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(h)]
#     visited = [[0] * w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             if matrix[i][j] == 1:
#                 dfs(i, j)
#                 res += 1
#     print(res)

# 여기는 방문했다는걸 왜 체크 안하지? 걍 방문하면 바로 지워버리는듯
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)