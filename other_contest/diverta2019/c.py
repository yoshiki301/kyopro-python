N = int(input())
res = 0
b_, _a, b_a = 0, 0, 0

for i in range(N):
    s = input()
    res += s.count("AB")
    s = s.replace("AB", "*")
    if s[0] == "B":
        if s[-1] == "A":
            b_a += 1
        else:
            b_ += 1
    elif s[-1] == "A":
        _a += 1

if b_a > 0:
    res += b_a - 1
    if _a > 0:
        res += 1
        _a -= 1
    if b_ > 0:
        res += 1
        b_ -= 1

res += min(_a, b_)
print(res)
