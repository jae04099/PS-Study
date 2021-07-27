# 한 회의가 끝나자 마자 다음 회의가 이어서 시작될 수 있다.
# 회의 시작, 끝 시간이 같을 수 있다.
# 끝나는 시간을 먼저 오름차순으로 맞추고 그 다음 시작시간 기준으로 오름차순 정렬하면 될듯

n = int(input())
lists = []
res = 1
for i in range(n):
    lists.append(list(map(int, input().split())))
lists.sort(key=lambda x:(x[1], x[0]))
start = lists[0]
for i in range(1, n):
    if start[1] <= lists[i][0]:
        res += 1
        start = lists[i]
print(res)