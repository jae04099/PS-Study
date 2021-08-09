# import sys

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# n=int(sys.stdin.readline())
# a=[list(sys.stdin.readline()) for _ in range(n)]
# cnt=0
# apt=[]

# def dfs(x,y):
#     global cnt
#     a[x][y] = '0' #방문한 곳은 0으로
#     cnt+=1
#     for i in range(4):
#         nx = x + dx[i] #i=0일때 (nx,ny)는 좌 , i=1일때 (nx,ny)는 상
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >=n:
#             continue
#         if a[nx][ny] == '1':
#             dfs(nx,ny)

# for i in range(n):
#     for j in range(n):
#         if a[i][j] == '1':
#             cnt= 0
#             dfs(i,j)
#             apt.append(cnt)

# print(len(apt))
# apt.sort()
# for i in apt:
#     print(i)

    # https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-2667%EB%B2%88-%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-%EC%B4%88%EC%BD%94%EB%8D%94



# import sys
# input = sys.stdin.readline

# n = int(input())
# # 데이터 저장용(기본적으로 받은 아파트 맵)
# matrix = [[0]*n for _ in range(n)]
# # 방문 내역 저장용
# visited = [[0] * n for _ in range(n)]

# # matrix에 아파트 유무 0과 1 저장
# for i in range(n):
#     line = input().strip()
#     for j, b in enumerate(line):
#         matrix[i][j] = int(b)

# # 방향 확인용 좌표 dx, dy
# # 중앙을 기준으로 좌/우/위/아래
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# #dfs

# def dfs(x, y, c):
#     visited[x][y] = 1   # 방문 여부 표시
#     global nums # 아파트 단지 수 세기 위한 변수
#     # 아파트 있으면 숫자 세기
#     if matrix[x][y] == 1:
#         nums += 1

#     # 아파트가 있는 시작점부터 깊이 탐색 시작
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 이동한 숫자가 경계에 넘는지 안넘는지. 넘으면 위 아래 옆 다 확인. 그렇지 않다면
#         if 0 <= nx < n and 0 <= ny < n:
#             # 방문 안했고 아파트가 있다면(단지인거임)
#             if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
#                 # 또 연결된 단지 찾아서
#                 dfs(nx, ny, c)

# cnt = 1 #아파트 단지 세기 위함
# numlist = []    # 아파트 단지별 숫자
# nums = 0    # 아파트 수
# for a in range(n):
#     for b in range(n):
#         # 방문은 안했는데 아파트가 있을 때
#         if matrix[a][b] == 1 and visited[a][b] == 0:
#             dfs(a, b, cnt)
#             numlist.append(nums)
#             nums = 0
#             cnt += 1    # 아파트 단지 별 표시

# print(len(numlist)) # 단지 수
# for n in sorted(numlist):
#     print(n)    # 단지 내 집의 수


# n = int(input())
# visited = [[0] * n for _ in range(n)]
# matrix = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# for _ in range(n):
#     x = list(map(int, input()))
#     matrix.append(x)
# cnt = 0
# apt_num = []

# def dfs(x, y):
#     global cnt
#     visited[x][y] = 1
#     cnt += 1
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny <= n:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
#                 cnt += 1
#                 dfs(nx, ny)

# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             dfs(i, j)
#             cnt = 0
#             apt_num.append(cnt)


# 왜 틀린지 모르겠음
# 프린트 하면 cnt가 계속 더해지는데...........


n = int(input())
matrix = []
visited = [[0] * n for _ in range(n)]
cnt = 0
res = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    lists = list(map(int, input()))
    matrix.append(lists)

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for i in res:
    print(i)