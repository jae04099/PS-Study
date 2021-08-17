# 수 3개로 연도. 지구(e), 태양(s), 달(m)
# 1 <= e <= 15, 1 <= s <= 28, 1 <= m <= 19
# 1년 = 1 1 1, 1년이 지날 때 마다 세 수는 모두 1씩 증가함
# 15년 = 15 15 15
# 16년 = 1 16 16 , e의 범위를 초과하기 때문임
# 주어진 esm에서 우리가 알고 있는 연도로 변환시키기
# 공배수 이런건가?
# 하나씩 1을 다 더해서 이상 이하 나오면 빼기

# 입력: 1 16 16, 출력: 16
# 입력: 1 1 1, 출력: 1
# 입력: 1 2 3, 출력: 5266
# 입력: 15 28 19, 출력: 7980

e, s, m = map(int, input().split())
sam_e, sam_s, sam_m = 1, 1, 1
cnt = 0

while True:
    cnt += 1
    if sam_e == e and sam_s == s and sam_m == m:
        break
    sam_e += 1
    if sam_e > 15:
        sam_e -= 15
    sam_s += 1
    if sam_s > 28:
        sam_s -= 28
    sam_m += 1
    if sam_m > 19:
        sam_m -= 19
print(cnt)
