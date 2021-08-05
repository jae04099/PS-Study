n, p = map(int, input().split())

d = [0 for _ in range(1000)]
d[1] = n
answers = [d[1]]
deleted = []

def dfs(n):
    for i in range(2, n):
        a = list(map(int, str(d[i - 1])))
        d[i] = sum(x**p for x in a)
        if d[i] not in answers:
            answers.append(d[i])
        else:
            deleted.append(d[i])
            break


dfs(1000)
idx = answers.index(deleted[0])
del answers[idx:]
print(len(answers))

'''
D는 {57, 74(=5^2+7^2=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …}
p = 2
d[1] = 57
d[2] = 74
d[3] = 7^2 + 4^2 = 49 + 16 = 65
d[4] = 6^2 + 5^2 = 36 + 25 = 61
d[5] = 6^2 + 1^2 = 36 + 1 = 37
'''