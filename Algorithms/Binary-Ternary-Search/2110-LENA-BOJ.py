# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로.

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lists = sorted(list(int(input()) for _ in range(n)))

start, end = 1, max(lists) - 1

while start <= end:
    mid = (start + end) // 2
    wifi = min(lists) + mid
    cnt = 1
    for i in range(1, len(lists)):
        if wifi <= lists[i]:
            cnt +=1
            wifi = lists[i] + mid
    if cnt >= c:
        start = mid + 1

    else:
        end = mid - 1
print(end)
