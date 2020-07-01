import math

H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

res = [[0]*W for i in range(H)]
cur = [0, 0]

# 蛇行しながら埋めていく
for i, ai in enumerate(a):
    while ai > 0:
        res[cur[0]][cur[1]] = (i + 1)
        if cur[1] % 2 == 0:
            if cur[0] == (H-1):
                cur[1] += 1
            else:
                cur[0] += 1
        else:
            if cur[0] == 0:
                cur[1] += 1
            else:
                cur[0] -= 1
        ai -= 1

str_n = int(math.log10(N)) + 2

for i in range(H):
    for j in range(W):
        print(str(res[i][j]).ljust(str_n), end="")
    print("")