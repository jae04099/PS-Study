#출처[https://infinitt.tistory.com/288]
from sys import stdin

N = int(input())
arr_n = list(map(int,stdin.readline().split()))
M = int(input())
arr_m = list(map(int,stdin.readline().split()))

dic = dict()

for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# a.sort()

# def binary(i):
#     start, end = 0, n-1
#     count = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if i > a[mid]:
#             start = mid + 1
#         elif i < a[mid]:
#             end = mid - 1
#         else:
#             end = mid - 1
#             count += 1
#     return str(count)

# answer = ''
# for i in b:
#     answer += binary(i)

# print(' '.join(answer))