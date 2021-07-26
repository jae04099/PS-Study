# n 2 m 1 한팀 원칙
# 대회 참여하려는 사람 중 k명은 반드시 인턴십 참여
# 최대 팀의 수는?
# 인턴쉽(k) 참여자를 남자에서도, 여자에서도 둘 다 에서도 빼보기?
# 만약 인턴십 참여자가 5명이라면 0, 5 / 1, 4 / 2, 3 이런식으로 다 뺀 후에 최댓값 ㄱㄱ

# n, m, k = map(int, input().split())
# res = 0
# cnt = 1
# for i in range(k):
#     # 일단 인턴십 참여자 수를 뺌
#     if n - i >= 2 and m - (k - i) >= 1:
#         n -= i
#         m -= (k - i)
#         # 아래 부등호를 >로 하면 맨 처음 테스트 통과가 안됨. >=로 하면 마지막 테스트 통과가 안됨.
#         while n // (2 * cnt) > 0 and m - cnt >= 0:
#             n /= (2 * cnt)
#             m -= cnt
#             cnt += 1
#         if res < cnt:
#             res = cnt
#         cnt = 1
# print(res)

n, m, k = map(int, input().split())
cnt = 0
while n + m >= k and n >= 0 and m >= 0:
    n -= 2
    m -= 1
    cnt += 1
    # 0이 될 때 까지 해서 1을 뺴나
print(cnt - 1)

# 굳이 인턴십 인원을 먼저 뺴버리지 말고 포용하는 방법을 쓰는듯?
# 가끔은 단순하게 생각 할 필요가 있다
