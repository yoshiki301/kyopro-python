N, K = map(int, input().split())
pN = list(map(int, input().split()))

# 期待値の累積和を利用
ex_p = [(pi+1)/2 for pi in pN]
cum_p = [ex_p[0]]
for i in range(1,N):
    cum_p.append(cum_p[i-1]+ex_p[i])

max_ex = cum_p[K-1]
for i in range(1,N-K+1):
    if max_ex < cum_p[K+i-1] - cum_p[i-1]:
        max_ex = cum_p[K+i-1] - cum_p[i-1]

print(max_ex)


