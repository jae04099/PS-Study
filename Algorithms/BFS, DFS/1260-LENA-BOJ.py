# dfs는 stack, bfs는 queue
# n = 정점의 개수, m = 간선의 개수, v = 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
matrix = [[0]*(n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0] * (n+1)