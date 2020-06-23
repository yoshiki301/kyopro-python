import math

N = int(input())

i = int(math.sqrt(N))
m = N % i

while m != 0:
    i -= 1
    m = N % i

A = int(math.log10(i))
B = int(math.log10(N//i))

res = max(A,B) + 1

print(res)