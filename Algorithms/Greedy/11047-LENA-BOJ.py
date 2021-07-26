# 테스트 케이스는 맞았는데 틀림
# 값이 모두 나누어떨어진다는 말이 없어서 그것도 검사해야하나?
# n, k = map(int, input().split())
# result = 0
# lists = []
# for i in range(n):
#     lists.append(int(input()))
# lists.reverse()
# for i in lists:
#     if k > i:
#         result += k // i
#         k %= i
#         if k == 0:
#             break
# print(result)

n, k = map(int, input().split())
result = 0
lists = []
for i in range(n):
    lists.append(int(input()))
lists.reverse()
for i in lists:
    # 같거나 크다는것을 적지 않음
    if k >= i :
        result += k // i
        k %= i
        if k == 0:
            break
print(result)
