import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Bの各要素に対してA, C上で二分探索して数える
    # lower_bound = bisect_left
    # upper_bound = bisect_right
    sA = sorted(A)
    sC = sorted(C)

    res = 0
    for b in B:
        a = bisect.bisect_left(sA, b)
        c = N - bisect.bisect_right(sC, b)
        res += a*c

    print(res)

if __name__ == "__main__":
    main()