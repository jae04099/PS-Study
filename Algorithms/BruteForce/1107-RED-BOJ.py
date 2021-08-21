#출처 [https://pacific-ocean.tistory.com/424]
import sys
input = sys.stdin.readline
def check(num):
    num = list(str(num))
    for i in num:
        if i in s: return False
    return True
n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)
for i in range(1000001):
    if check(i): result = min(result, len(str(i)) + abs(i - n))
print(result)

# target = list(int(i) for i in str(input()))
# n = int(input())
# cur = 100
# T = int(''.join(list(map(str, target))))

# if n == 0:
#     op = 0
#     while cur != T:
#         if cur < T:
#             cur += 1
#         else:
#             cur -= 1
#         op += 1

#     print(op)
# else:
#     m = set(map(int, input().split()))
#     p = set(i for i in range(10)) - m
#     answer = list()

#     def find_near(arr, t):
#         minValue = min(arr, key = lambda x: abs(x - t))
#         return minValue

#     for i in target:
#         if i not in m:
#             answer.append(i)
#         else:
#             answer.append(find_near(list(p), i))

#     a = int(''.join(list(map(str, answer))))
    
#     op = 0
#     tmp = [cur, a]
#     found = find_near(tmp, T)

#     if found == 100:
#         answer.clear()
        
#     while found != T:
#         if found < T:
#             found += 1
#         else:
#             found -= 1

#         op += 1

#     print(len(answer) + op)


# '''
# cur = 100

# target = 5457
# 3
# 6 7 8

# 1 2 3
# 4 5 x
# x x 9
# + 0 -

# 5, 4, 5, 5, +, +

# ======

# 422
# 8
# 0 2 3 4 6 7 8 9

# 1 x x
# x 5 x
# x x x
# + 0 -

# 5 1 1

# '''
