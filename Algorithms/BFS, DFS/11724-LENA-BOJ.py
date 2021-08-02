# 궁금점: bfs dfs를 모두 사용하라는 문제가 아니라면 어떤걸 써도 답이 나오는건가?
# 언제 무엇을 써야할지 문제마다 내가 선택해야하는건가...?

n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
cnt = 0
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(i):
    visited[i] = 1
    for k in range(1, n + 1):
        if matrix[i][k] == 1 and visited[k] == 0:
            dfs(k)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
