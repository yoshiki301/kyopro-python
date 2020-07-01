N = int(input())
AB = []
for _ in range(N):
    ab = list(map(int, input().split()))
    AB.append(ab)

# 期限が早い順にソートして貪欲
AB.sort(key=lambda x:x[1])
sum_t = 0

for ab in AB:
    sum_t += ab[0]
    if sum_t > ab[1]:
        print("No")
        exit()

print("Yes")