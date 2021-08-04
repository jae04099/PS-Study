'''
참고 [https://claude-u.tistory.com/435]
1 2 3 4 5 6 7
3 1 3 7 3 4 6

g[1] = 3
g[3] = 3
g[3] = 3, can_loop = 3

g[2] = 1
g[1] = 3
g[3] = 3, can_loop = 3

g[3] = 3, can_loop = 3

g[4] = 7
g[7] = 6
g[6] = 4
g[4] = 7, can_loop = 4
g[7] = 6, can_loop = 4, 7
g[6] = 4, can_loop = 4, 7, 6
'''
import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸 !!  이게 포인트
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수

# import sys
# sys.setrecursionlimit(10000)

# def dfs(graph, can_loop, root):
#     if graph[root] not in can_loop:
#         dfs(graph, can_loop, graph[root])



# def solution():
#     n = int(input())
#     graph = dict()
#     students = map(int, input().split())
#     i = 1
#     for s in students:
#         graph[i] = s
#         i += 1
    
#     count = 0
#     for g in graph:
#         print(dfs(graph, g))
#         count += 1
#             # dfs(graph, visited, g)
    
#     print(count)

# T = int(input())

# for _ in range(T):
#     solution()


'''
양방향 그래프
루프만들기..
1
7
3 1 3 7 3 4 6


1 2 3 4 5 6 7
3 1 3 7 3 4 6

g[1] = 3
g[3] = 3
g[3] = 3, visited = 3

g[2] = 1
g[1] = 3
g[3] = 3, vsited = 3

g[3] = 3, visited = 3

g[4] = 7
g[7] = 6
g[6] = 4
g[4] = 7, visited = 4
g[7] = 6, visited = 4, 7
g[6] = 4, visited = 4, 7, 6

반례)

1 2 3 4
2 3 4 3

1 - 2
2 - 3
3 - 4
4 - 3

g[1] = 2
g[2] = 3
g[3] = 4
g[4] = 3
g[3] = visited

(3, 4)

'''