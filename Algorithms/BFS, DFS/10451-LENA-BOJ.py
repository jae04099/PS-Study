# 순열 사이클이 있다는 것은 시작점과 끝점이 같을 때
# (3, 2)랑 (2, 3)이 다 1일때?
# import sys
# sys.setrecursionlimit(2000)

# t = int(input())
# def dfs(v):
#         visited[v] = 1
#         num = numbers[v]
#         if not visited[num]:
#             dfs(num)

# for i in range(t):
#     n = int(input())
#     res = 0
#     visited = [0] * (n + 1)
#     lists = list(map(int, input().split()))
#     matrix = [[0] * (n + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         matrix[i][lists[i]] = 1
    # 제일 깊이 들어갔는데 결국 그 끝이 처음 값 이라면 한 사이클 아닐까? 때문에 dfs를 써야하지 않을까?

# =============================================
# dfs를 한 번 실행할 때 마다 cnt 값을 올려주면 사이클 개수를 확인할 수 있다.

# import sys
# sys.setrecursionlimit(10000)

# input = sys.stdin.readline

# # 이어 진 것은 dfs 한 바퀴 쭉 돌 테니...
# def dfs(start):
#     visited[start] = True
#     next_path = path[start]
#     if not visited[next_path]:
#         dfs(next_path)
# # 아마 앞에 붙인 0 + 어쩌구 true + 어쩌구는 0이 아닌 1 인덱스부터 시작하려고 그런 것 같음
# for _ in range(int(input())):
#     n = int(input())
#     path = [0] + list(map(int, input().split()))
#     visited = [True] + [False] * n
#     ans = 0

#     for i in range(1, n + 1):
#         if not visited[i]:
#             dfs(i)
#             ans += 1
#     print(ans)


import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    next = lists[v]
    if not visited[next]:
        dfs(next)

for i in range(input()):
    n = int(input())
    visited = [True] + [False] * n
    res = 0
    lists = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            res += 1
    print(res)

