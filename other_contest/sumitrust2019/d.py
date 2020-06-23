N = int(input())
S = input()

res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            i_ok = False
            j_ok = False
            k_ok = False
            check = str(i)
            for l in range(N):
                if S[l] == check:
                    if not i_ok:
                        i_ok = True
                        check = str(j)
                    elif not j_ok:
                        j_ok = True
                        check = str(k)
                    elif not k_ok:
                        k_ok = True
                        break
    
            if i_ok and j_ok and k_ok:
                res += 1

print(res)