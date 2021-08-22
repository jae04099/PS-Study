# 또 bfs 느낌이 든ㄷㅏ...
# n으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는가
# +를 누르면 +1 채널로 / -를 누르면 -1 채널로 / 0에서 -1 누르면 0 / 채널은 무한대
# 번호 버튼을 눌러도 되고 +, - 버튼을 눌러도 되는데 이게 최적이려면 다 해봐야 하는듯? (브루트포스)
# 최대한 숫자로 해결가능할 때 까지 하고 그 다음에 플마 쓰나?
# 현재 채널: 100 / 이동하려는 채널 n
# from collections import deque

# target = int(input())
# start = 100
# n = int(input())
# errKey = list(map(int, input().split()))
# numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# canUse = [x for x in numList if (x not in errKey)]
# q = deque([[start, 0]])
# # res = 6

# while q:
#     chaNum, cnt = q.popleft()
#     if chaNum == target:
#         print(cnt)
#         break
#     for i in range(len(target)):
#         for j in (canUse):
            
#===================================================
# 과몰입 했는데 결국엔 순수 브루트포스였음
# https://javaiyagi.tistory.com/585

target = int(input())
start = 100
n = int(input())
errKey = list(map(str, input().split()))
numList = [str(i) for i in range(10)]
# numlist에서 errkey 뺀 값
canUse = [x for x in numList if (x not in errKey)]

# 최소 버튼을 눌러야 하는 횟수 초기화. 
min_cnt = abs(start - target)

# 100만번 반복하는 이유는 50만이 최대이지만 +가 최적일때랑 -가 최적일떄 다를 것 이기 때문임
# 0번 채널부터 ㄱㄱ
for chan in range(1000000):
    for j in range(len(str(chan))):
        # 현재 자릿수에 누를 수 없는 버튼이 있다면 패스
        if str(chan)[j] not in canUse:
            break
        elif len(str(chan)) - 1 == j:
            min_cnt = min(min_cnt, abs(chan - n) + len(str(chan)))
print(min_cnt)


# https://pacific-ocean.tistory.com/424

import sys
input = sys.stdin.readline
# 해당 자릿수가 고장난 번호인지 아닌지 check 함수
def check(num):
    num = list(str(num))
    for i in num:
        if i in s: return False
    return True
n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)
for i in range(1000001):
    if check(i): result = min(result, len(str(i)) + abs(i - n))
print(result)


# https://velog.io/@sangjin98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1107%EB%B2%88-%EB%A6%AC%EB%AA%A8%EC%BD%98

target = int(input())
M = int(input())
numberList = {str(i) for i in range(10)} # 입력 불가능한 번호들을 제거해주기 위해 리스트가 아닌 set로 선언

if M != 0:
    numberList -= set(map(str, input().split())) # 입력 불가능한 숫자들 제외

start = 100
count = abs(start - target) # 모든 숫자가 입력이 불가능할 경우(+, - 로만 이동하는 경우)가 입력 횟수 최대의 경우 이므로
                            # 입력 횟수를 저장하는 변수를 최대의 경우로 선언

for i in range(1000000): # 고장날 버튼과 희망채널의 관계를 고려하여 최악의 경우 100만까지 순회해야하므로 범위를 100만까지 지정
    for j in range(len(str(i))): # 현재 순회중인 채널의 각 자릿수를 조회
        if str(i)[j] not in numberList: # 현재 자릿수의 숫자가 입력 불가능한 숫자이면 다시 순회하러 감
            break
        elif j == len(str(i)) - 1: # 모든 자릿수가 입력 가능한 숫자이면
            count = min(count, abs(i - target) + len(str(i))) # 이전에 구한 입력 횟수보다 적다면 최소 입력횟수를 변경

print(count)