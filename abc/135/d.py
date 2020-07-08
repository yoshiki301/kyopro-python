def main():
    mod = 1000000007
    S = input()
    n = len(S)

    # dp[i][j] 左からi文字目までの数で, 余りがjになるものの総数
    # for多すぎてpypyしか勝たん
    dp = [[0] * 13 for i in range(n)]

    s = S[0]
    if s == "?":
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(s)] = 1

    for i in range(1,n):
        s = S[i]
        if s == "?":
            for rem in range(10):
                for pre in range(13):
                    dp[i][(10*pre + rem) % 13] += dp[i-1][pre]
                    dp[i][(10*pre + rem) % 13] %= mod

        else:
            rem = int(s)
            for pre in range(13):
                    dp[i][(10*pre + rem) % 13] += dp[i-1][pre]
                    dp[i][(10*pre + rem) % 13] %= mod

    res = dp[n-1][5]
    print(res)


if __name__ == "__main__":
    main()