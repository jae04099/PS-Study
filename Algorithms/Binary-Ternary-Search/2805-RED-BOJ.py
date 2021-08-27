n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in a:
        if i > mid:
            tmp += i - mid
        
    if tmp >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)