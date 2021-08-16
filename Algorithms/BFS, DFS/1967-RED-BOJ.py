#https://chldkato.tistory.com/29
from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n)]
    c[x] = 0
    while q:
        x = q.popleft()
        for w, nx in a[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

n = int(input())
a = [[] for _ in range(n)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    a[x-1].append([w, y-1])
    a[y-1].append([w, x-1])
print(bfs(bfs(0, 1), 2))

# #출처[https://developmentdiary.tistory.com/436]

# import sys
 
# V=int(sys.stdin.readline())
 
# matrix=[[] for _ in range(V+1)]

# for _ in range(V):
#     path = list(map(int,sys.stdin.readline().split()))
#     # path_len=len(path)
#     # for i in range(1,path_len//2):
#     matrix[path[0]].append([path[1], path[2]])
 
 
# #첫번째 DFS결과
# result1 = [0 for _ in range(V+1)]
 
# def DFS(start,matrix,result):
#     for e,d in matrix[start]:
#         if result[e]==0:
#             result[e]=result[start]+d
#             print('dfs')
#             DFS(e,matrix,result)
 
# DFS(1,matrix,result1)#아무노드에서 시작해준다.
# result1[1] = 0#루트노드가 정해져 있지않아 양방향으로 입력을 받기때문에 해당
 
 
# tmpmax=0#최대값 구하기
# index=0#최장경로 노드
 
# for i in range(len(result1)):
#     if tmpmax<result1[i]:
#         tmpmax=result1[i]
#         index=i
 
# #최장경로 노드에서 다시 DFS를 통해 트리지름구하기
# result2=[0 for _ in range(V+1)]
# DFS(index,matrix,result2)
# result2[index]=0
# print(max(result2))
