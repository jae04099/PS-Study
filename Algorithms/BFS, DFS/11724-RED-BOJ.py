#출처 [https://velog.io/@devjuun_s/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EB%B0%B1%EC%A4%80-11724%EB%B2%88python]
#Pypy3 로 할것
import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)

# from collections import deque

# graph = {}
# n, m = map(int, input().split())

# for i in range(m):
#     n1, n2 = map(int, input().split())
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)


# def bfs(graph, root):
#     visited = []
#     queue = deque([root])

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort()
#                 queue += temp
#     return set(visited)

# answers = []
# for i in range(1, n+1):
#     answers.append(list(bfs(graph, i)))

# answers = list(set([tuple(set(answer)) for answer in answers]))

# print(len(answers))

    

'''
### 2차원 리스트 중복제거 [https://inma.tistory.com/132]
연결요소란? [https://velog.io/@kjh107704/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C]
6 5

1 2
2 5
5 1
3 4
4 6


    1 - 2 - 5
    3 - 4 - 6
'''