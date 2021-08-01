# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램
# {0, 1, 2, 4, 3, 5} 라고 할 때, 0 + 1 + (2 * 3) + (4 * 5) 라고 묶어야 최댓값 됨.
# 수열의 모든 수는 단 한번만 묶거나 묶지 않아야 함(?)

# -와 +를 곱하면 안됨. -와 -는 곱해도 됨.
# 0은 곱하면 안되니 일단 remove 시키고 본다

# n = int(input())
# plusLists = []
# lists = []
# absLists = []
# for i in range(n):
#     lists.append(int(input()))

# absLists = sorted(lists, key=abs)
# absLists.reverse()
# lists.sort()

# if 0 in absLists:
#     absLists.remove(0)

# i = 1
# while i < n:
#     if absLists[i - 1] * absLists[i] > 0:
#         plusLists.append(absLists[i - 1] * absLists[i])
#         i += 2
#     else:
#         plusLists.append(absLists[i - 1])
#         i += 1
# print(sum(plusLists))

#=========================================================

# 숫자의 분류를 잘 시키는 것이 관건이었음.
# 양수 리스트, 음수 리스트, 0이나 1인 경우(0은 곱하면 안됨. 1은 더하는게 곱보다 더 큼)

n = int(input())
pn = []
nn = []
en = []

for i in range(n):
    num = int(input())
    if num > 1:
        pn.append(num)
    elif num < 0:
        nn.append(num)
    else:
        en.append(num)

pn.sort(reverse=True)
nn.sort()

result = 0
if len(pn) % 2 == 0:
    for i in range(0, len(pn) - 1, 2):
        result += pn[i] * pn[i + 1]
if len(pn) % 2 != 0:
    for i in range(0, len(pn) - 1, 2):
        result += pn[i]*pn[i + 1]
    result += pn[-1]

if len(nn) % 2 == 0:
    for i in range(0, len(nn) - 1, 2):
        result += nn[i] * nn[i + 1]
if len(nn) % 2 != 0:
    for i in range(0, len(nn) - 1, 2):
        result += nn[i]*nn[i + 1]
    if 0 not in en:
        result += nn[-1]
        # 0이 있으면 0을 nn[-1]과 곱하는 것이 최댓값 아닌가? 왜 0 유무 따지다가 말지? 정답은 맞음
result += sum(en)
print(result)

# https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1744%EB%B2%88-%EC%88%98-%EB%AC%B6%EA%B8%B0