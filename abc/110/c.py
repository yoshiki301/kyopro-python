S = input()
T = input()

s_t = {}
s = set()
t = set()
for i in range(len(S)):
    if S[i] not in s:
        if T[i] not in t:
            s.add(S[i])
            t.add(T[i])
            s_t[S[i]] = T[i]
        else:
            print("No")
            exit()
    else:
        if s_t[S[i]] != T[i]:
            print("No")
            exit()

print("Yes")