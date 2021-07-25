#출처 [https://suri78.tistory.com/105]
a = list(map(int, input().split()))
N = a[0]
k = a[1]
mod = 1000000000

table = [1]
table += [0] * N

for _ in range(1, k+1):
    for idx in range(1, N+1):
        table[idx] = (table[idx] + table[idx-1])%mod

print(table[N])

# a = list(map(int, input().split()))

# N = a[0]
# k = a[1]

# print(1 + N*(k-1))

'''
BOJ2225
20 2
0 + 20
1 + 19
2 + 18
…
19 + 1
20 + 0
= 21

3 1
3
= 1

3 2
0 + 3
..
3 + 0
= 4

3 3
0 + 1 + 2
0 + 2 + 1
1 + 0 + 2
1 + 2 + 0
2 + 0 + 1
2 + 1 + 0
1 + 1 + 1
0 + 0 + 3
…
3 + 0+ 0
= 10

4 1
4
= 1

4 2
0 + 4
…
4 + 0
 = 5

'''