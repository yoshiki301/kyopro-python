N, M = map(int, input().split())
S, C = [], []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

res = ["?"] * N

# そのままやる, 一番左の0に注意する
for i in range(M):
    if S[i]-1 == 0 and C[i] == 0 and N > 1:
        print(-1)
        exit()
    elif res[S[i]-1] == "?":
        res[S[i]-1] = str(C[i])
    elif res[S[i]-1] != str(C[i]):
        print(-1)
        exit()

if res[0] == "?" and N > 1:
    res[0] = "1"
elif res[0] == "?" and N == 1:
    res[0] = "0"

res = "".join(res)
res = res.replace("?", "0")

print(res)