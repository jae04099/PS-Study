N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(len(a) - 1):
    if a[i] < 10001 and a[i] > 1 and a[i + 1] > 1:
        a[i] *= a[i+1]
        a[i+1] = 10001

a = list(filter((10001).__ne__, a))
a.sort()

for i in range(len(a) - 1):
    if a[i] < 10001 and a[i] <= 0 and a[i + 1] <= 0:
        a[i] *= a[i+1]
        a[i+1] = 10001

a = list(filter((10001).__ne__, a))
print(sum(a))

'''
반례 1)

6

-5
-2
-1
0
3
6

output:31
answer:28
'''