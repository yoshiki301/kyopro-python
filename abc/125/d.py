N = int(input())
A = map(int, input().split())

A_plus = []
A_minus = []

for a in A:
    if a >= 0:
        A_plus.append(a)
    else:
        A_minus.append(a)

A_plus = sorted(A_plus)
A_minus = sorted(A_minus)


if len(A_minus) % 2 == 0:
    res = sum(A_plus) - sum(A_minus)
else:
    if len(A_plus) > 0:
        res = sum(A_plus) - sum(A_minus) - 2*min(A_plus[0], (-1)*A_minus[-1])
    else:
        res = sum(A_plus) - sum(A_minus) + 2*A_minus[-1]

print(res)