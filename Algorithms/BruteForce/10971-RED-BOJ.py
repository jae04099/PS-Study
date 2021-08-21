import itertools

n = int(input())
a = list()
for i in range(n):
    a.append(list(map(int, input().split())))

print(a)
'''
https://limdongjin.github.io/problemsolving/boj_10971_%EC%99%B8%ED%8C%90%EC%9B%90%EC%88%9C%ED%9A%8C2.html#%E1%84%91%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B52-itertools-permutations-%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%AD%E1%86%BC
import itertools
import sys
input = sys.stdin.readline
def main():
    n = int(input())
    costs = [[0]*n for _ in range(n)]
    for y in range(n):
        s = list(map(int, input().split()))
        for i in range(n):
            costs[y][i] = s[i]

    perms = itertools.permutations(range(n))
    ret = sys.maxsize
    for perm in perms:
        if costs[perm[-1]][perm[0]] == 0:
            continue
        cost = 0
        flag = True
        for i in range(n-1):
            from_v = perm[i]
            to_v = perm[i+1]
            if costs[from_v][to_v] == 0:
                flag = False
                break
            cost += costs[from_v][to_v]
            if cost >= ret:
                flag = False
                break
        if flag == False:
            continue
        cost += costs[perm[-1]][perm[0]]
        ret = min(ret, cost)

    print(ret)

main()
'''