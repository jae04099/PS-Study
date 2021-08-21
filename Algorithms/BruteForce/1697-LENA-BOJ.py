# n - 1, n + 1, 2 * n 중에 어떤걸 사용해야 동생을 찾을 수 있는 제일 빠른 시간?
# 수빈 위치 > 동생 위치 : n - 1만 가능
# 수빈 위치 == 동생 위치: return 0
# 수빈 위치 < 동생 위치: 셋 다 써도 됨


# n, k = map(int, input().split())
# time = 0

# if n == k :
#     print(0)
# elif n < k :
#     print(k - n)
# else:
#     while n != k:


# 왜 bfs지?
# from collections import deque

# def bfs():
#     q = deque()
#     q.append(n)
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(dist[x])
#             break
#         for nx in (x - 1, x + 1, x * 2):
#             if 0 < nx <= MAX and not dist[nx]:
#                 dist[nx] = dist[x] + 1
#                 q.append(nx)

# MAX = 10 ** 5
# dist = [0] * (MAX + 1)
# # 수빈, 동생
# n, k = map(int, input().spilt())

# bfs()



# from collections import deque

# def bfs():
#     q = deque()
#     q.append(n)
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(res_arr[x])
#             break
#         for nx in(x - 1, x + 1, 2 * n):
#             # 0 == False
#             if 0 < nx <= MAX and not res_arr[nx]:
#                 res_arr[nx] = res_arr[x] + 1
#                 q.append(nx)

# MAX = 10**5
# res_arr = [0] * (MAX + 1)
# n, k = map(int, input().split())


from collections import deque

def dfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(res_list[x])
            break
        for nx in (x + 1, x - 1, 2 * x):
            if 0 < nx <= MAX and not res_list[nx]:
                res_list[nx] = res_list[x] + 1
                q.append(nx)

n, k = map(int, input().split())
MAX = 10**5
res_list = [0] * (MAX + 1)

dfs()