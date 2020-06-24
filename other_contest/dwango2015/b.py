import re

S = input()

replaced = S.replace("25","a")
nico_list = re.split(r'[0-9]+', replaced)

res = 0
for nico in nico_list:
    n = len(nico)
    res += n*(n+1)//2

print(res)