# k, n = map(int, input().split())
# lists = list(int(input()) for _ in range(k))
# # 1, 802
# start, end = 1, max(lists)

# while start <= end:
#     # 401
#     mid = (start + end) // 2
#     lan_num = 0
#     for i in lists:
#         lan_num += i // mid
#     if lan_num >= n:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# lists = list(int(input()) * n)

# start, end = 1, max(lists)
# while start <= end:
#     mid = (start + end) // 2
#     lan_num = 0
#     for i in lists:
#         lan_num += i // mid
#     if lan_num >= n:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lists = list(int(input()) for _ in range(n))
start, end = 1, max(lists)

while start <= end:
    mid = (start + end) // 2
    res = 0
    # 모든 갖고있는 랜선의 길이를 다 카운트 셈
    for i in lists:
        res += i // mid
    # 그래서 나온 총 개수로 판단
    if res >= n:
        start = res + 1
    else:
        end = res - 1
print(end)

# n = 4
# k = 11
# lists = [802, 743, 457, 539]

# 1:
# start = 1, end = 802
# mid = 401
# res = 0

# 1-1:
# res = 2
# start = 1
# end = 