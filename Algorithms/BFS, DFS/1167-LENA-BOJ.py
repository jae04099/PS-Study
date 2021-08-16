# https://sdesigner.tistory.com/48
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다

# 3 1 2 4 3 == 3이랑 1이 이어져있고 길이는 2, 3이랑 4가 이어져있고 길이는 3
# 정점까지의 거리를 알려주는 그래프를 만들면 어차피 그게 연결 돼 있다는 것 과 마찬가지 아님?

# 정점의 개수
# n = int(input())
# lists = [[0] * (n + 1) for _ in range(n + 1)]
# matrix = [list(map(int, input().split())) for _ in range(n + 1)]
# # 일단 매트릭스에 받아놓고 생각해보기.

# for i in matrix:
#     for j in range(len(i)):
#         if i[j] == -1:
#             break
#         lists[i[0]][j]
        

# ===================================================

import sys
input = sys.stdin.readline

n = int(input())
node_graph = [[] for _ in range(n + 1)]
for i in range(n):
    path = list(map(int, input().split()))
    path_len = len(path)
    for i in range(1, path_len//2):
        node_graph[path[0]].append([path[2*i - 1], path[2*i]])
# [[], [[3, 2]], [[4, 4]], [[1, 2], [4, 3]], [[2, 4], [3, 3], [5, 6]], [[4, 6]]]
result_first = [0 for _ in range(n+1)]

def dfs(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            dfs(e, matrix, result)

dfs(1, node_graph, result_first)
result_first[1] = 0

tmpmax = 0
index = 0

for i in range(len(result_first)):
    if tmpmax < result_first[i]:
        tmpmax = result_first[i]
        index = i

result_final = [0 for _ in range(n + 1)]
dfs(index, node_graph, result_final)
result_final[index] = 0
print(max(result_final))