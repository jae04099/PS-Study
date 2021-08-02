# dfs는 stack, bfs는 queue
import collections
# n = 정점의 개수, m = 간선의 개수, v = 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
# n개의 정점을 가지는 그래프를 인접 행렬로 표현하기 위해서는 간선의 수와 무관하게 항상 n^2개의 메모리 공간이 필요함.
# n + 1을 한 이유는 0이 아니라 1부터 시작해서 헷갈리지 않게 하기 위함이다.
mat = [[0] * (n + 1) for _ in range(n + 1)]
# 방문한 곳 체크를 위한 배열 선언
visited = [0] * (n + 1)
# 입력 받는 두 값에 대해 영행렬에 1 삽입
for i in range(m):
    a, b = map(int, input().split())
    mat[a][b] = mat[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        # 방문하지 않았으면서 인접행렬이 맞으면 1 체크 위한 재귀 실행
        if mat[v][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = collections.deque
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if mat[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

dfs(v)
# 이미 dfs에서 처리 한 것을 0으로 리셋
visited = [0] * (n + 1)
print()
bfs(v)
