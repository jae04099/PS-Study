target = str(input())
n = int(input())
m = list(map(int, input().split()))

cur = '100'
answer = list()
# if target == '100' or target == '101' or target == '102' or target == '99' or target == '98':

for i in target:
    if i not in m:
        answer.append(i)


'''
cur = 100

target = 5457
3
6 7 8

1 2 3
4 5 x
x x 9
+ 0 -

5, 4, 5, 5, +, +

======

422
8
0 2 3 4 6 7 8 9

1 x x
x 5 x
x x x
+ 0 -

5, 0, 0, -x87

'''
