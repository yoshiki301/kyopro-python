N, K = map(int, input().split())

if N == 1:
    res = 1
elif N == 2:
    res = 1 / 2
else:
    if K == 1 or K == N:
        res = 3 * ((K-1) + (N-K)) # 2つK
        res += 1 # 3つK
        res /= N ** 3
    else:
        res = 3 * 2 * (K-1) * (N-K) # 1つK
        res += 3 * ((K-1) + (N-K)) # 2つK
        res += 1 # 3つK
        res /= N ** 3

print(res)