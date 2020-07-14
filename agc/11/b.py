import math
import collections
import itertools
import heapq

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 降順にソートして a_{i} <= a_{i+1}から末項までの累積和ならインクリメント
    revs_A = sorted(A, reverse=True)
    double_A = sorted(list(map(lambda x: 2*x, A)))
    cum_double_A = list(itertools.accumulate(double_A))[::-1]
    res = 1
    for i, a in enumerate(cum_double_A[1:]):
        if a >= revs_A[i]:
            res += 1
        else:
            break
    print(res)

if __name__ == "__main__":
    main()