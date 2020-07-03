N = int(input())
a = list(map(int, input().split()))

# 要素をチェックし, 単調増加になっている数nとして n*(n+1)//2を足す
res = 0
check = 0
n = 0
for ai in a:
    if check >= ai:
        res += n*(n+1)//2
        n = 1
    else:
        n += 1
    check = ai

res += n*(n+1)//2
print(res)