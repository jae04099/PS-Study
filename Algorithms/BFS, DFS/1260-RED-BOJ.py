from collections import deque

def dfs(graph, root):
    stack = [root]
    visited = list()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    
    return visited

def bfs(graph, root):
    #"앞으로 찾아야 가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색
    queue = deque([root])
    visited = list()
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort()
                queue += temp
            
    return visited



graph = dict()

n, m, v = map(int, input().split())

for i in range(m):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(' '.join(str(x) for x in dfs(graph, v)))
print(' '.join(str(x) for x in bfs(graph, v)))

#참고 [https://itholic.github.io/python-bfs-dfs/]
#참고2 [https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html]

# from collections import deque

# def DFS(graph, root):
#     visited = []
#     stack = [root]

#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort(reverse=True)
#                 stack += temp
#     return " ".join(str(i) for i in visited)

# def BFS(graph, root):
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
#     return " ".join(str(i) for i in visited)

  
# graph = {}
# n = input().split(' ')
# node, edge, start = [int(i) for i in n]
# for i in range(edge):
#     edge_info = input().split(' ')
#     n1, n2 = [int(j) for j in edge_info]
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)

# print(DFS(graph, start))
# print(BFS(graph, start))