import sys
input = sys.stdin.readline
n = int(input())    # 5
cards = sorted(list(map(int, input().split()))) # 6 3 2 10 -10
m = int(input())    # 8
nums = list(map(int, input().split()))   # -10 -5 2 3 4 5 9 10

def binary(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            return print(1, end=' ')
        elif target > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return print(0, end=' ')

for i in range(m):
    binary(nums[i])


