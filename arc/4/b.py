N = int(input())
max_d = 0
min_d = 0

# pypyだとメモリに乗り切らない(!?)
for i in range(N):
    d = int(input())
    if d > max_d:
        min_d = d - max_d
    else:
        min_d = max(min_d - d, 0)
    max_d += d

print(max_d)
print(min_d)