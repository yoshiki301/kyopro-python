n = int(input())
a = list(map(int, input().split()))

# nは最大値, rはn/2に最も近い要素
sorted_a = sorted(a)
a_max = sorted_a[-1]

dif = []
for i,ai in enumerate(sorted_a[:n-1]):
    dif.append((i,abs(ai-(a_max/2))))

min_i = sorted(dif, key=lambda x:x[1])[0][0]
dif_min = sorted_a[min_i]

print(a_max, dif_min)