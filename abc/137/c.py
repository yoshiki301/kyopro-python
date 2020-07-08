def main():
    N = int(input())
    # 文字列をソートしてdictに保存
    s_dict = {}
    for _ in range(N):
        s = input()
        s_sort = "".join(sorted(list(s)))
        if s_sort not in s_dict:
            s_dict[s_sort] = 0
        s_dict[s_sort] += 1

    res = 0
    for v in s_dict.values():
        res += v*(v-1)//2

    print(res)


if __name__ == "__main__":
    main()