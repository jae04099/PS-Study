# n = int(input())
# stairs = []
# res1 = [0] * n
# res2 = [0] * n

# for i in range(n):
#     stairs.append(int(input()))

# for i in range(3, n):
#     res1[i] = (max(stairs[i] + stairs[i - 2], stairs[i - 1]))
#     res2[i] = (max(stairs[i - 1] + stairs[i - 3], stairs[i - 2]))
# print(res1)
# print(res2)

# n = int(input())
# lists = []
# dp = [0] * n

# for i in range(n):
#     lists.append(int(input()))

#     # 이 아래의 세가지는 3미만 인덱스의 것들은 계산을 못 하는 것에서 착안
# dp.append(lists[0])
# dp.append(max(lists[0]+lists[1], lists[1]))
# dp.append(max(lists[0]+lists[2], lists[1] + lists[2]))

# for i in range(3, n):
#     dp.append(max(lists[i] + lists[i - 1] + dp[i - 3], lists[i] + dp[i - 2]))
# print(dp)

# 다들 n-1, n-3이라고 하는데 그냥 마지막꺼는 나중에 더해주고 n-2, n-1 + n-3 하면 안됨?

import sys 
input = sys.stdin.readline 
arr = [] 
dp = [] 
l = int(input()) 
for _ in range(l): 
    arr.append(int(input())) 
dp.append(arr[0]) 
dp.append(max(arr[0]+arr[1],arr[1])) 
dp.append(max(arr[0]+arr[2],arr[1]+arr[2])) 
for i in range(3,l): 
    dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1])) 
print(dp.pop())

# max(o x o, o x o o)
# 건너뛰는 것 기준, 이전 값은 저장해 둔 값이어야하기에 dp 인덱스를 사용한다.