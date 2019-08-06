def print_rues(rues):
    1
    # print("--")
    # for l in range(0, q + 1):
    #     print("\t {}".format(rues[l]))


t = int(input())  # read a line with a single integer


def change_max(x, y, maxim, x2, y2, val):
    if val < maxim:
        return x, y, val
    if val > maxim or x2 < x or x2 == x and y2 < y:
        return x2, y2, val
    return x, y, val


for i in range(1, t + 1):
    p, q = map(int, input().split())

    x, y = 0, 0
    inter = [[0] * (q + 1) for _ in range(q + 1)]

    maxim = 0

    for j in range(0,p):
        xjs, yjs, dj = input().split()
        xj = int(xjs)
        yj = int(yjs)

        # print(xj, yj, dj)

        if dj == 'N':
            for xd in range(0, q + 1):
                for k in range(yj + 1, q + 1):
                    inter[xd][k] += 1
                    print_rues(inter)
                    x, y, maxim = change_max(x, y, maxim, xd, k, inter[xd][k])
        if dj == 'S':
            for xd in range(0, xj + 1):
                for k in range(0, yj):
                    inter[xd][k] += 1
                    print_rues(inter)
                    x, y, maxim = change_max(x, y, maxim, xd, k, inter[xd][k])

        if dj == 'E':
            for yd in range(0, yj + 1):
                for k in range(xj + 1, q + 1):
                    inter[k][yd] += 1
                    print_rues(inter)
                    x, y, maxim = change_max(x, y, maxim, k, yd, inter[k][yd])
        if dj == 'W':
            for yd in range(0, q + 1):
                for k in range(0, xj):
                    inter[k][yd] += 1
                    print_rues(inter)
                    x, y, maxim = change_max(x, y, maxim, k, yd, inter[k][yd])

        # print("##")
        # for l in range(0, q):
        #     print("\t {}".format(inter[l]))


    # print(inter)

    # print("####")
    # for l in range(0, q):
    #     print("\t {}".format(inter[l]))

    print("Case #{}: {} {}".format(i, x, y))


# Expected
# Case #1: 0 6
# Case #2: 2 5
# Case #3: 0 4
