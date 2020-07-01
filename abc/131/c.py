import math

A, B, C, D = map(int, input().split())

# 共通部分はlcm(C,D)であることに注意する
b = B - ((B // C) + (B // D) - (B // (C*D // math.gcd(C,D)))) 
a = A-1 - (((A-1) // C) + ((A-1) // D) - ((A-1) // (C*D // math.gcd(C,D))))
res = b - a
print(res)