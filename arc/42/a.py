N, M = map(int, input().split())

# aを逆から見てthreadから削除しsetにしてくっつける
thread = [i for i in range(1,N+1)]
a = []
for i in range(M):
    a.append(int(input()))

a = set(a[::-1])
thread = set(thread) - a

res = list(a) + list(thread)

for i in range(N):
    print(res[i])

