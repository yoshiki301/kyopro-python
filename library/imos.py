# 1次元, N回シミュレート, M個のクエリ
N, M = map(int, input().split())

simulate = [0]*(N+1)

# 入退出
for i in range(M):
    l, r = map(int, input().split())
    simulate[l-1] += 1
    simulate[r] -= 1

# シミュレート
res = 0
count = 0
for i in range(N):
    count += simulate[i]
    if count == M: # 判定の条件
        res += 1