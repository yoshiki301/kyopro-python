N, M = map(int, input().split())

k = []
s = []
for i in range(M):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])

p = list(map(int, input().split()))

# 全探索で間に合う
switch = [0]*N

res = 0
for i in range(1<<N):
    div = i
    for j in range(N):
        switch[j] = div % 2
        div //= 2

    on = True
    for l in range(M):
        s_state = 0
        for s_check in s[l]:
            s_state ^= switch[s_check-1]
        if s_state != p[l]:
            on = False
    
    if on:
        res += 1

print(res)