x = int(input())

case = list(map(int, input().split()))

increase = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)

decrease2 = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            decrease2[i] = max(decrease2[i], decrease2[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease2[i] -1 

print(max(result))

# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4