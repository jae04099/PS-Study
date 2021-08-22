import itertools

n = int(input())

a = list(map(int, input().split()))

def solution(p):
    answer = 0
    for i in range(len(p) - 1):
        answer += abs(p[i] - p[i+1])

    return answer

b = list(itertools.permutations(a))

answers = []
for p in b:
    answers.append(solution(p))

print(max(answers))
'''
6
20 1 15 8 4 10
'''