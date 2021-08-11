

# #출처 [https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-2667%EB%B2%88-%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-%EC%B4%88%EC%BD%94%EB%8D%94#recentEntries]

# import sys
# sys.setrecursionlimit(10000)

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# n=int(input())
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

# # N = int(input())

# # a = list()

# # for i in range(N):
# #     a.append(list(''.join(str(input()))))

# # for i in range(N):
# #     for j in range(N):
# #         a[i][j] = int(a[i][j])

# # count = 0
# # for i in range(1, N - 1):
# #     count += 1
# #     for j in range(1, N - 1):
# #         if a[i][j] == 1:
# #             a[i][j] += count
# #             if a[i-1][j] == 1:
# #                 a[i-1][j] += count
# #             elif a[i][j-1] == 1:
# #                 a[i][j-1] += count
# #             elif a[i][j+1] == 1:
# #                 a[i][j+1] += count
# #             elif a[i+1][j] == 1:
# #                 a[i+1][j] += count
# #     print(count)

# # print(a)

