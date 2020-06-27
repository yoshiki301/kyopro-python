S_dash = input()
T = input()

if len(S_dash) < len(T):
    print("UNRESTORABLE")
    exit()

# 反転して先頭からマッチング, 他のものはaで埋める
else:
    res = "UNRESTORABLE"
    rev_S = S_dash[::-1]
    rev_T = T[::-1]
    for i in range(len(rev_S)-len(rev_T)+1):
        check = rev_S[i:i+len(rev_T)]
        t_ok = [False] * len(rev_T)
        for j, (c, t) in enumerate(zip(check, rev_T)):
            if c == t or c == "?":
                t_ok[j] = True
        if sum(t_ok) == len(t_ok):
            res = list(rev_S)
            for j,t in enumerate(rev_T):
                res[i+j] = t
            res = "".join(res[::-1])
            res = res.replace("?", "a")
            print(res)
            exit()

    print(res)
                