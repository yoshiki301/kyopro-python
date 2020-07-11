def calc(x, y, z):
    return (x**2 + y**2 + z**2 + x*y + y*z + z*x)

def main():
    N = int(input())

    val = [0] * 100000

    # 全探索
    for x in range(1,101):
        for y in range(1,101):
            for z in range(1,101):
                val[calc(x,y,z)] += 1

    for i in range(1,N+1):
        print(val[i])

if __name__ == "__main__":
    main()
