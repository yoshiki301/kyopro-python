def main():
    A, B = map(int, input().split())

    # 偶数nに対して, n^(n+1) = 1であることを用いる
    res = 0
    if A % 2 == 0 and B % 2 == 1:
        res = ((B - A + 1) // 2) % 2
    elif A % 2 == 0 and B % 2 == 0:
        res = (((B - A) // 2) % 2)^B
    elif A % 2 == 1 and B % 2 == 0:
        res = (((B - A - 1) // 2) % 2)^A^B
    else:
        res = (((B - A) // 2) % 2)^A

    print(res)

if __name__ == "__main__":
    main()