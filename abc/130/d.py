N, K = map(int, input().split())
a = list(map(int, input().split()))

s = t = total = 0
res = 0
while True:
    while t < N and total < K:
        total += a[t]
        t += 1
    if total < K:
        break
    res += N - t + 1
    total -= a[s]
    s += 1
 
print(res)