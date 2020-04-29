import math

def solve():
    W, H, L, U, R, D = [int(s) for s in input().split()]

    row = [0 if U == 1 and L - 1 <= i else pow(2, -i) for i in range(W)]

    complement = 0

    for j in range(1, H):
        next = [ -1 for _ in range(W)]

        for i in range(W):
            if L - 1 <= i <= R - 1 and U-1 <= j <= D-1:
                next[i] = 0
            else:
                next[i] = \
                    (0 if i == 0 else next[i - 1] / (2 if j < H - 1 else 1)) + \
                    (row[i] / (2 if i < W - 1 else 1))

        row = next
    return row[W-1]


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):

        print("Case #{}: {}".format(case, solve()))

