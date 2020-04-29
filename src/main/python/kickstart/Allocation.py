def solve(n, b):
    houses = sorted([int(s) for s in input().split()])

    y = 0
    for h in houses:
        if h <= b:
            y += 1
            b -= h
        else:
            return y
    return y


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        n, b = [int(s) for s in input().split()]

        print("Case #{}: {}".format(case, solve(n, b)))

