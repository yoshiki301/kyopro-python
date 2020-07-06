import math

N, H = map(int, input().split())
a, b = [], []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

a_max = sorted(a)[-1]
b_des = sorted(b, reverse=True)

res = 0
sum_b = 0
for bi in b_des:
    if bi <= a_max:
        break
    else:
        H -= bi
        res += 1
    if H <= 0:
        break

if H > 0:
    res += int(math.ceil(H / a_max))

print(res)