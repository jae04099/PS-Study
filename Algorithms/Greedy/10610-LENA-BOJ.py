# 양수 n을 조합해서 30의 배수를 만들 되 가장 큰 30의 배수 만들기
# 30의 배수는 3의 배수이면서 일의 자리가 0이어야함

# import itertools

# n = input()
# res = -1
# lists = []
# for i in n:
#     lists.append(i)
# perlists = list(map(''.join, itertools.permutations(lists)))
# for i in perlists:
#     if i[-1] == '0' and int(i) % 3 == 0:
#         if res < int(i):
#             res = int(i)
# print(res)
# =============================================================
# 위 코드 정답은 맞는데 메모리 초과 뜸

# 3의 배수는 곧 각 자리 숫자들을 더했을 때 3으로 나누어 떨어져야함
# 때문에 0이 있고 각 자리 숫자들의 합이 3으로 나누어 떨어진다는 조건이 맞으면 오름차순으로 정렬한 수가 비교하지 않아도 제일 큰 수가 된다.

n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
    # 일의 자리수가 0이어야 한다는 것은 0이 필수로 있어야 한다는 말임
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))
