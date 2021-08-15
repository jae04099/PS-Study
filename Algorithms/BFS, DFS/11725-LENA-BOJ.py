# 루트없는 트리가 주어질 때 트리의 루트는 1.
# 각 노드의 부모 구하기

# n = int(input())
# matrix = [[0] * (n + 1) for _ in range(n + 1)]
# # visited로 체크하면 두갈래나 세갈래같은건 카운트를 못함
# visited = [0] * (n + 1)
# result = [0] * (n + 1)
# for i in range(n - 1):
#     a, b = map(int, input().split())
#     matrix[a][b] = 1

# def dfs(root):
#     visited[root] = 1
#     for i in range(1, n + 1):
#         if matrix[root][i] == 1 and result[i] == 0:
#             result[i] = root
#             dfs(i)
# dfs(1)
# for i in range(2, n + 1):
#     if visited[i] == 0:
#         dfs(i)
        
# print(result)    

# ===================================================
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n + 1)]

# 정답이 담길 array
parents = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    # 연결된걸 인덱스, 원소로 저장.
    # 트리는 무방향 그래프임
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    # 연결된 노드들로부터 parents[i]의 부모가 없으면 부모 설정 해줌
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, n+1):
    print(parents[i])