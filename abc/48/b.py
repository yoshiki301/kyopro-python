a, b, x = map(int, input().split())

if a == 0:
    res = b // x + 1
else:
    res = (b // x) - ((a-1) // x)

print(res)
