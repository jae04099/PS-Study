#[출처] https://pacific-ocean.tistory.com/194
s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i - 2] * 2) + s[i - 1])
n = int(input())
print(s[n] % 10007)

#import itertools
# import operator as op
# from functools import reduce #[참고] https://www.daleseo.com/python-functools-reduce/

# def nCr(n, r, sq):
#     print(n , r)
#     r = min(r, n-r)
#     numerator = reduce(op.mul, range(n, n - r, -1), 1)
#     denominator = reduce(op.mul, range(1, r+1), 1)
#     denominator2 = reduce(op.mul, range(1, sq+1), 1)
#     return numerator // denominator*denominator2

# dp = []

# for sq in range(n//2+1):
#     if sq == n//2:
#         dp.append(1)
#         break
#     for i in range(n+1):
#         if i == 0 or i%2 == 0:
#             dp.append(nCr(int(n - i/2 - sq/2), int(i/2), sq))

# print(sum(dp)%10007)