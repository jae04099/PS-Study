import sys
sys.setrecursionlimit(10000)

def dfs(graph, visited, v):
    visited[v] = True
    if not visited[graph[v]]:
        dfs(graph, visited, graph[v])

def solution():
    N = int(input())
    graph = dict()
    visited = dict()
    count = 0

    nodes = map(int, input().split())

    i = 1
    for n in nodes:
        graph[i] = n
        visited[i] = False
        i += 1
    
    count = 0
    for j in graph:
        if not visited[j]: # visited == False
            dfs(graph, visited, j)
            count += 1

    print(count)

T = int(input())

for _ in range(T):
    solution()


# from collections import deque

# def bfs(graph, root):
#     queue = deque([root])
#     visited = list()

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             # if n in graph.keys():
#             queue += [graph[n]]
    
#     return visited


# def solution():
#     N = int(input())
#     nodes = map(int, input().split())

#     i = 1
#     for n in nodes:
#         graph[i] = n
#         i += 1

#     answers = list()
#     for i in range(1, N):
#         a = bfs(graph, graph[i])
#         answers.append(a)

#     answers = list(set([tuple(set(answer)) for answer in answers]))

# graph = dict()

# T = int(input())

# for _ in range(T):
#     solution()