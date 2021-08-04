# d[1] = a
# d[n] = d[n-1]의 각 자리의 숫자를 p번 곱한 수들의 합
# a ** b (a의 b제곱)

# 리스트를 계속 append를 하다가 리스트에 같은 것이 나오면 스탑?
# 반복되지만 반복 리스트가 아닌 경우도 있을까?

# a, p = map(int, input().split())
# lists = []
# a = str(a)
# target = 0
# pin = 0
# i = 0
# def cal(n):
#     target = 0
#     for i in range(len(n)):
#         target += int(n[i]) ** p
#     return target
# cal(a)
# while target != lists[i]:
#     if target in lists:
#         pin = target
#         break

# https://suri78.tistory.com/127
import sys
input = sys.stdin.readline
a, p = map(int, input().split())
seq = [a]

while True:
    t = seq[-1]
    val = 0
    while t:
        val += ((t%10) ** p)
        t //= 10
    
    if val in seq:
        input(str(seq.index(val)))
        break
    else:
        seq.append(val)

# https://ywtechit.tistory.com/63

a, p = map(int, input().split())
res = [a]

while True:
    temp = sum([int(i) ** p for i in str(a)])
    if temp in res:
        break
    res.append(temp)
    a = temp

print(res.index(temp))