mod = 998244353

N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    res = 0
else:
    dict_D = {}
    for d in D:
        if d not in dict_D:
            dict_D[d] = 0
        dict_D[d] += 1

    max_D = sorted(D)[-1]

    res = 1
    parent = 1
    for i in range(max_D+1):
        if i == 0:
            if dict_D[0] != 1:
                res = 0
                break
        else:
            if i not in dict_D:
                res = 0
                break
            else:
                if i != 1:
                    res *= (parent**dict_D[i])
                    res %= mod
                parent = dict_D[i]

print(res)

