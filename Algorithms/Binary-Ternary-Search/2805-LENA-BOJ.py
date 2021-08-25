# 20 15 10 17
# 높이=15
# 15 15 10 15
# 5인 나무와 2인 나무를 들고 집에 갈 것(총 7미터)

# pypy3로 통과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lists = list(map(int, input().split()))
start, end = 1, max(lists)
mid = 0
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

while start <= end:
    res = 0
    mid = (start + end) // 2
    for i in lists:
        if (i - mid) >= 0:
            res += i - mid
    if res >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)