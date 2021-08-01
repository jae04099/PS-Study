N = int(input())
p = list(map(int, input().split()))

p.sort()

answer = 0
answers = []
for i in p:
    answer += i
    answers.append(answer)

print(sum(answers))