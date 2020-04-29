def solve(n, d):
    buses = [int(s) for s in input().split()]

    start = d
    for b in buses[::-1]:
        start -= start % b
    return start


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        n, d = [int(s) for s in input().split()]

        print("Case #{}: {}".format(case, solve(n, d)))

