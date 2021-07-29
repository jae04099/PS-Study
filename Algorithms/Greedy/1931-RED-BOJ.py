N = int(input())
a = []
answers = []
for i in range(N):
    a.append(tuple(map(int, input().split())))

a.sort(key=lambda x:(x[1], x[0]))

cur = a[0][1]
count = 1
for i in range(N-1):
    if cur <= a[i+1][0]:
        count += 1
        cur = a[i+1][1]
print(count)
# for j in range(N):
#     cur = a[j][1]
#     count = 1
#     for i in range(j, N - 1):
#         if cur <= a[i+1][0]:
#             count += 1
#             cur = a[i+1][1]
#     answers.append(count)
# print(max(answers))
'''
(1,3)
(3,4)
가능 
BOJ1931

[ 1;4, 5;7
[ 3;5, 6;10(둘다넣을수 잇으면 가장큰거)
[ 0;6,
[ 3;8,
[ 5;9



1;4, 5;7, 8;11 12;14
3;5, 6;10 …

…
2;13, 
12; 14

반례
15
1 4
7 7
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
7 7
7 7
7 7
2 13
12 14

7,7 의 경우 여러번 할 수 있는듯..
'''