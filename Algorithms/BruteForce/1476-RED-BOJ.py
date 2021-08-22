E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
year = 1

while True:
    if e == E and s == S and m == M:
        break

    year += 1
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
        
print(year)
'''
15 15 15 => 15
1 16 16 => 16
2 17 17 => 17
3 18 18 => 18
4 19 19 => 19
5 20 1 => 20

'''
