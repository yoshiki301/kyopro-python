N = int(input())
a = []
for i in range(N):
    ai = int(input())
    a.append(ai)

# 座標圧縮, もう少しやり方がありそう
itr = 0
a_to_b = {}
check_a = -1
for ai in sorted(a):
    if check_a == ai:
        continue
    else:
        a_to_b[ai] = itr
        itr += 1
        check_a = ai

for ai in a:
    print(a_to_b[ai])