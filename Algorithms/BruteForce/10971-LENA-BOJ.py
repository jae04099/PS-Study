# 외! 판! 원!
# 한 도시에서 출발해 n개의 도시를 모두 거쳐 다시 원 도시로 돌아오는 순회 여행 경로 계획.
# 예시로는 4곳을 방문해야함
# 한 번 갔던 도시로는 다시 갈 수 없음
# 비용은 행렬로 주어짐, w[i][j] = 도시 i에서 j로 가기 위한 비용
# w[i][j]랑 w[j][i]는 다를 수 있음
# dp + dfs?

# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# for i in range(n):
#     visited[i][i] = 1


# def dfs(x, y):
#     visited[x][y] = 1
#     # 갈 수 있는 위 아래 왼 오중에 가장 값싸게 이동할 수 있는 부분은 어디지?
#     for i in range(4):
#         a, b = dx[i] + x, dy[i] + y
#         if 0 <= a < n and 0 <= b < n and matrix[x][y] != 0:
#             matrix[a][b] = min(matrix[x][y] + matrix[a][b])

#====================================================
# dp방법, dfs방법이 있었음
# 백트래킹이라는게 있었음. 그 알고리즘은 dfs와 혼동하기 쉬운데, memoization처럼 유망하지 않은 경우의 수는 줄이는걸 목표로 한다 함.
# https://jjangsungwon.tistory.com/4
# dfs
import sys


def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()


if __name__ == "__main__":

    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    # 각 번호에서 시작
    for i in range(N):
        dfs(i, i, 0, [i])

    print(min_value)

# 백트래킹
N=int(input())
W=[list(map(int,input().split()))for i in range(N)]
V=[0]*N
M=1e10
def back_track(n,c):
    global N,W,V,M
    if c<M:
        if all(V) and n==0:
            M=min(M,c)
        for i in range(N):
            if W[n][i]>0 and not V[i]:
                V[i]+=1
                back_track(i,c+W[n][i])
                V[i]-=1
back_track(0,0)
print(M)

# https://velog.io/@dlskawns96/Python-%EB%B0%B1%EC%A4%80-10971%EB%B2%88-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%99%982

import sys

n = int(input())

costs = [[0] * n for _ in range(n)]
for i in range(n):
    costs[i] = list(map(int, input().split()))

def dfs(start, v, visited, value):
    global min_value

    if len(visited) == n:
        if costs[v][start] != 0:
            min_value = min(min_value, value + costs[v][start])
        return
    
    for i in range(n):
        if i != start and costs[v][i] != 0 and i not in visited:
            visited.append(i)             # 방문 처리를 하고,
            value += costs[v][i]
            dfs(start, i, visited, value) # 다음 도시로 이동,
            value -= costs[v][i]
            visited.pop()                 # 그 도시의 모든 경우를 확인 하고, pop -> 다음 도시로

min_value = sys.maxsize
for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i, i, [i], 0)
    
print(min_value) 