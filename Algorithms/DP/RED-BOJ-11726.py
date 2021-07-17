n = int(input())

#import itertools
import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

dp = []

for i in range(n+1):
    if i == 0:
        dp.append(1)
        continue
    if i%2 == 0:
        dp.append(nCr(int(i/2 + n - i), int(i/2)))
        # vertical = n - i
        #dp.append(len(list(itertools.combinations(range(1, int(i/2 + n - i)+ 1), int(i/2)))))

print(sum(dp)%10007)
