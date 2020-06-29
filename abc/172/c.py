N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cumA = [0] * (N+1)
cumB = [0] * (M+1)

point = 0
for i in range(N):
    cumA[i+1] = cumA[i] + A[i]
for i in range(M):
    cumB[i+1] = cumB[i] + B[i]

# 尺取りの要領でiを増やしjを減らす
res, j = 0, M
for i in range(N+1):
    if cumA[i] > K:
        break
    while cumB[j] > K - cumA[i]:
        j -= 1
    res = max(res, i+j)

print(res)