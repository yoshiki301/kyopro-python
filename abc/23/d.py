def det(x, hs, n):
    sec = [(x-hs[i][0])//hs[i][1] for i in range(n)]
    sec = sorted(sec)
    for i, s in enumerate(sec):
        if i > s:
            return False
    return True


def main():
    N = int(input())
    HS = [list(map(int, input().split())) for i in range(N)]

    # 判定問題に置き換えて探索範囲を狭めていく
    l = 0
    u = 10**16
    while u - l > 1:
        mid = (u+l) // 2
        if det(mid, HS, N):
            u = mid
        else:
            l = mid

    print(u)

if __name__ == "__main__":
    main()