# 이동 가능 루트 = [[-2, 1], [-1, 2], [1, 2], [2, 1]]
# 세로 n 가로 m
# 이동횟수 따져서 4번보다 같거나 많다면 4개 방법 다 이용해야함.
# n, m = map(int, input().split())
# chess = [[0] * m for _ in range(n)]
# now = chess[0][n - 1]
# cnt = 0
# movement = [[-2, 1], [-1, 2], [1, 2], [2, 1]]

# =============================================================
# 세로가 1이면 위, 아래로 가는 어떤 방법도 사용할 수 없으니 1 리턴
# 세로가 2이면 1칸 위 아래 가는 방법만 사용할 수 있다.
# n이 3보다 작거나 m이 7보다 작은 경우 이동 횟수가 4번이 되지 않을 것.
# 본인은 위치를 기록하려고 했으나 그렇게 할 필요 없고 그냥 숫자로 계산하면 됨

# 직접 그림을 봐야 이해가 됨
# 근데 min을 왜 쓰는지 이해가 안감. 4를 넘으면 넷 다 써야해서?

n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1)//2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m - 2)

    # https://cijbest.tistory.com/6