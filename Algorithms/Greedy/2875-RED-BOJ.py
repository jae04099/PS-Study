inputs = list(map(int, input().split()))

n = inputs[0]
m = inputs[1]
k = inputs[2]

if m == 0:
    print(0)
else:
    while k > 0:
        if n >= m*2:
            n -= 1
            k -= 1
        else:
            m -= 1
            k -= 1

if n > m*2:
    print(m)
else:
    print(int(n/2))

#print(int(n/2)) 실패
# 반례 5 1 1 => n = 4, m = 1