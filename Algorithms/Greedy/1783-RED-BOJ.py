#출처 [https://5w33th0me4jisu.tistory.com/entry/Python-1783-%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8-1]

n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m - 2)
'''

!!! 방문할 수 있는 칸!!
즉,
= = a +
o + + +

o, a 두개뿐 = > 2

BOJ1783

2 x 4

+ + + +
o + + +
x

=> 4

???

17 x 5

+ + + + +
+ + + + +
+ + + + +
…
+ + + = =
+ + + = +
+ + = = +
+ + = + +
= = = + +
o + + + +

=> 10 ???

'''