import heapq

def main():
    N, M = map(int, input().split())
    a_to_b = {}
    for i in range(N):
        a, b = map(int, input().split())
        if a <= M:
            if a not in a_to_b:
                a_to_b[a] = []
            a_to_b[a].append(b)

    # 最終日から見て可能な報酬をヒープで管理, 最大値をとってくる
    res = 0
    h = []
    for i in range(1,M+1):
        if i in a_to_b:
            b_list = a_to_b[i]
            for bi in b_list:
                heapq.heappush(h, (-1)*bi) # 最大値をpopするときは負数で管理
        if len(h) > 0:
            res -= heapq.heappop(h)

    print(res)


if __name__ == "__main__":
    main()