N = int(input())

res = 0
if N % 2 == 0:
    div = N // 2
    for i in range(1,30):
        res += div // 5**i

print(res)
