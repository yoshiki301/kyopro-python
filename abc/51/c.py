sx, sy, tx, ty = map(int, input().split())

dist_x = tx - sx
dist_y = ty - sy

res = "R" * dist_x + "U" * dist_y + "L" * dist_x + "D" * dist_y + "D" + "R" * (dist_x + 1) + "U" * (dist_y + 1) + "L" + "U" + "L" * (dist_x + 1) + "D" * (dist_y + 1) + "R"
print(res)