def solve():
    W, H, L, U, R, D = [int(s) for s in input().split()]

    grid = [[ -1 for row in range(H)] for col in range(W)]

    for i in range(L, R+1):
        for j in range(U, D+1):
            grid[i-1][j-1] = 0

    for i in range(W):
        for j in range(H):
            if i == 0 and j == 0:
                grid[i][j] = 1
            elif grid[i][j] != 0:
                grid[i][j] = \
                    (0 if i == 0 else grid[i-1][j] / (2 if j < H -1 else 1)) + \
                    (0 if j == 0 else grid[i][j-1] / (2 if i < W - 1 else 1))

    return grid[W-1][H-1]


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):

        print("Case #{}: {}".format(case, solve()))

