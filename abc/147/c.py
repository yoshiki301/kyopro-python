import itertools

def main():
    N = int(input())
    xy = [0] * N
    for i in range(N):
        A = int(input())
        xy_list = []
        for _ in range(A):
            x, y = map(int, input().split())
            xy_list.append((x, y))
        xy[i] = xy_list

    # bit全探索
    res = 0
    tf_gen = itertools.product([0, 1], repeat=N)
    for tf in tf_gen:
        honest = sum(tf)
        able = True
        for i, xy_l in enumerate(xy):
            for (x, y) in xy_l:
                if tf[x-1] != y and tf[i] == 1:
                    able = False
        if res < honest and able:
            res = honest
    print(res)


if __name__ == "__main__":
    main()