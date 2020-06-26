N, M = map(int, input().split())
card = [0]*(N+1)

# imos法

# 入退出
for i in range(M):
    l, r = map(int, input().split())
    card[l-1] += 1
    card[r] -= 1

# シミュレート
res = 0
gate = 0
for i in range(N):
    gate += card[i]
    if gate == M:
        res += 1

print(res)