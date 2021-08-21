# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
# 제일 큰 수 제일 작은수를 빼면 되지 않을까
# 절대값임
# 0 - 1 / 1 - 2 / 2 - 3이런식
from itertools import permutations

n = int(input())
lists = list(map(int, input().split()))
pers = list(permutations(lists, n))
res = -1
tmp = 0
for i in range(len(pers)):
    for j in range(1, n):
        tmp += abs(pers[i][j - 1] - pers[i][j])
    res = max(tmp, res)
    tmp = 0
print(res)