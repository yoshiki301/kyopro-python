H, W, K = map(int, input().split())

def to_int(s):
    if s == ".":
        return 0
    else:
        return 1

c = [0] * H
for i in range(H):
    c[i] = list(map(to_int, input()))

# bit全探索
res = 0
for h_bit in range(1<<H):
    for w_bit in range(1<<W):
        sum_c = 0
        h = h_bit
        for i in range(H):
            if h % 2 == 1:
                w = w_bit
                for j in range(W):
                    if w % 2 == 1:
                        sum_c += c[i][j]
                    w //= 2
            h //= 2
        if sum_c == K:
            res += 1
    
print(res)
