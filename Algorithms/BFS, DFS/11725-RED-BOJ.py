#출처[https://claude-u.tistory.com/192]
import sys

node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

#DFS나 BFS나 무관

def dfs(graph_list, start, parent):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent

for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])
# N = int(input())
# a = {}

# for i in range(N):

'''
7
1 6
6 3
3 5
4 1
2 4
4 7

2 - 4 - 1 - 6 - 3 - 5
4 - 7

        1
    4       6
2    7          3
                    5

1 : 4, 6
2 : 
3 : 5
4 : 2, 7
5: 
6 : 3
'''