from collections import defaultdict
N, M = map(int, input().split())
order = []
dd = defaultdict(int)

for i in range(M):
    p, y = map(int, input().split())
    order.append([i, p, y])

# 全体を年代順にソート
order.sort(key=lambda x: (x[2]))

res = defaultdict(str)
for i, pp, yy in order:
    dd[pp] += 1
    res[i] = str(pp).zfill(6) + str(dd[pp]).zfill(6)

for i in range(M):
    print(res[i])