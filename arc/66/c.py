import math
import collections
import itertools
import heapq
import bisect
import sys


def main():
    mod = 1000000007
    N = int(input())
    A = list(map(int, input().split()))

    exist = True
    res = 0
    if N % 2 == 0:
        check = [2] * (N // 2)
        for a in A:
            if a % 2 == 1:
                if check[(a-1)//2] > 0:
                    check[(a-1)//2] -= 1
                else:
                    exist = False
            else:
                exist = False
        if exist:
            res = 1
            for i in range(N//2):
                res *= 2
                res %= mod
    else:
        check = [2] * ((N+1) // 2)
        check[0] = 1
        for a in A:
            if a % 2 == 0:
                if check[a//2] > 0:
                    check[a//2] -= 1
                else:
                    exist = False
            else:
                exist = False
        if exist:
            res = 1
            for i in range((N-1)//2):
                res *= 2
                res %= mod

    print(res)

    
    

if __name__ == "__main__":
    main()