#출처 [https://claude-u.tistory.com/443]
k, n = map(int, input().split())
a = list()
for i in range(k):
    a.append(int(input()))

start, end = 1, max(a)

a.sort()

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in a:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= n: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
4 11
802
743
457
539
'''