N = int(input())
A = list(map(int, input().split()))

sA = sorted(A, reverse=True)

# 最大を1つ, それ以外は2つずつ大きいものから順に選べる, 奇数の時は最後は1つ
if N % 2 == 0:
    res = sum(sA[:N//2]) * 2 - sA[0]
else:
    res = sum(sA[:N//2]) * 2 - sA[0] + sA[N//2]

print(res)
