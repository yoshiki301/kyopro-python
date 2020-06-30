N = int(input())
lr = []

for i in range(N):
    x, l = map(int, input().split())
    lr.append((x-l,x+l))

# 一度見たアームについて, その右側だけを考えれば良い
res = 0
max_r = float("-inf")

sorted_lr = sorted(lr, key=lambda x:x[1])
for lr in sorted_lr:
    if max_r <= lr[0]:
        res += 1
        max_r = lr[1]

print(res)