#출처 [https://pacific-ocean.tistory.com/340]
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

# from itertools import permutations

# N = list(str(input()))
# answers = []

# for n in list(permutations(N)):
#     if int(''.join(map(str, n))) % 30 == 0:
#         answers.append(int(''.join(map(str, n))))

# if answers:
#     print(max(answers))
# else:
#     print(-1)