inputs = list(map(int, input().split()))
n = inputs[0]
k = inputs[1]
coins = []
count = 0
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

while k > 0:
    for coin in coins:
        if coin <= k:
            count += int(k/coin)
            k -= coin * int(k/coin)
            break
print(count)


# 반례 - 시간초과
# 1 100000000
# 1
# 위 경우 O(100000000)가 필요