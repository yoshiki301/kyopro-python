N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for i in range(M):
    b, c = map(int, input().split())
    BC.append([b,c])

A = sorted(A)
BC = sorted(BC, key=lambda x:x[1], reverse=True)

# Aを昇順, key=Cとして(B, C)を降順にソートして増えなくなるまで置換
a_itr = 0
bc_itr = 0
bc = BC[0]
while a_itr < N:
    if bc[0] == 0:
        bc_itr += 1
        if bc_itr < M:
            bc = BC[bc_itr]
        else:
            break
    else:
        if A[a_itr] < bc[1]:
            A[a_itr] = bc[1]
            a_itr += 1
            bc[0] -= 1
        else:
            break

print(sum(A))

