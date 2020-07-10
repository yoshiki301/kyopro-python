def main():
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    # p, qのうち小さいものをrで置き換えられないかどうか見ていく
    sorted_p = sorted(p, reverse=True)[:X]
    sorted_q = sorted(q, reverse=True)[:Y]
    sorted_r = sorted(r, reverse=True)

    p_itr, q_itr, r_itr = X-1, Y-1, 0
    
    while r_itr < C:
        look_p = sorted_p[p_itr]
        look_q = sorted_q[q_itr]
        look_r = sorted_r[r_itr]

        if look_p <= look_q and p_itr >=0:
            if look_p <= look_r:
                sorted_p[p_itr] = look_r
                p_itr -= 1
                r_itr += 1
            else:
                break

        elif q_itr >= 0:
            if look_q <= look_r:
                sorted_q[q_itr] = look_r
                q_itr -= 1
                r_itr += 1
            else:
                break

        else:
            break

    res = sum(sorted_p) + sum(sorted_q)
    print(res)

if __name__ == "__main__":
    main()