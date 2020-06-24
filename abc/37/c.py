N, K = map(int, input().split())
a = list(map(int, input().split()))

cusum = [0]*len(a)

cusum[0] = a[0]
for i in range(1,len(a)):
    cusum[i] = cusum[i-1] + a[i]

res = cusum[K-1]
for i in range(1,N-K+1):
    res += cusum[i+K-1] - cusum[i-1]

print(res)