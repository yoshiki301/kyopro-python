import math

def main():
    mod = 1000000007
    N = int(input())
    A = list(map(int, input().split()))

    # bitごとに0と1の数の積を計算し, 足していく
    A_max = sorted(A)[-1]
    if A_max == 0: # 真数に0を入れないようにする
        print(0)
        exit()
    bit_max = int(math.ceil(math.log2(A_max)))

    i = 0
    bit = 1
    res = 0
    while i <= bit_max:
        c_zero = 0
        c_one = 0
        for j in range(N):
            if A[j] & bit == 0:
                c_zero += 1
            else:
                c_one += 1
        m_bit = bit % mod
        res += m_bit*c_zero*c_one
        res %= mod
        i += 1
        bit<<=1
    print(res)

if __name__ == "__main__":
    main()