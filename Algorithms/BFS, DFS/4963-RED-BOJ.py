import sys
sys.setrecursionlimit(10000)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x,y):
    global cnt
    a[x][y] = 0
    cnt+=1
    for i in range(8):
        nx = x + dx[i] #i=0일때 (nx,ny)는 좌 , i=1일때 (nx,ny)는 상
        ny = y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if a[nx][ny] == 1:
            dfs(nx,ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    answer = []

    for i in range(h): # 행
        for j in range(w): # 열
            if a[i][j] == 1:
                cnt= 0
                dfs(i,j)
                answer.append(cnt)
    print(len(answer))