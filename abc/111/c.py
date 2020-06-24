from collections import Counter

n = int(input())
v = list(map(int, input().split()))

v0 = v[0:n-1:2]
v1 = v[1:n:2]

c0 = Counter(v0).most_common()
c1 = Counter(v1).most_common()

if len(set(v0)) == len(set(v1)) == 1:
    if c0[0] == c1[0]:
        res = len(v0)
    else:
        res = 0

else:
    if c0[0] != c1[0]:
        res = n - c0[0][1] - c1[0][1]
    else:
        res = min(n - c0[0][1] - c1[1][1], n - c0[1][1] - c1[0][1])

print(res)