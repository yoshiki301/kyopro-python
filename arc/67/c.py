def main():
    mod = 1000000007
    N = int(input())

    # エラトステネスの篩で素数マップを作って素因数をカウント
    prime = [1] * (N+1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2,N+1):
        if prime[i] == 1:
            p = i
            j = 2
            while p*j <= N:
                prime[p*j] = 0
                j += 1

    res = 1
    for i in range(2,N+1):
        if prime[i] == 1:
            p = i
            j = 1
            num = 0
            while p**j <= N:
                num += N // (p**j)
                j += 1
            res *= (num+1)
            res %= mod

    print(res)

if __name__ == "__main__":
    main()