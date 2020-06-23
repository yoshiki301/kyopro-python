import math

A, B = map(int, input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

A_prime = set(prime_factorize(A))
B_prime = set(prime_factorize(B))

res = A_prime & B_prime

print(len(res)+1)