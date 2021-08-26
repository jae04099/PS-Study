n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary(i):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if i > a[mid]:
            start = mid + 1
        elif i < a[mid]:
            end = mid - 1
        else:
            return '1'
    return '0'

answer = ''
for i in b:
    answer += binary(i)

print(' '.join(answer))