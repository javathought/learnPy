def solve(n):
    points = [int(s) for s in input().split()]
    peaks = 0
    for i in range(len(points) - 2):
        if points[i+1] > points[i] and points[i+1] > points[i+2]:
            peaks += 1
    return peaks


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        n = int(input())

        print("Case #{}: {}".format(case, solve(n)))

