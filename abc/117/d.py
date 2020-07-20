def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 答えは40bitで表現できる, 条件を満たすxを求める
    c = [0] * 40
    res = 0
    for a in A:
        for bit in range(40):
            if a & (1<<bit):
                c[bit] += 1

    x = 0
    for k in range(39,-1,-1):
        if x + (1<<k) > K:
            continue
        if c[k] <= N // 2:
            x += (1<<k)

    for a in A:
        res += x^a

    print(res)
  

if __name__ == "__main__":
    main()