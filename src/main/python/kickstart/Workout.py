from math import floor, ceil


def solve(n, k):
    w = [int(s) for s in input().split()]
    ecarts = [0 for _ in range(n-1)]
    for i in range(len(w)-1):
        ecarts[i] = w[i+1] - w[i]

    e = sorted(ecarts)
    ne = []

    d = 0

    for _ in range(k):
        a = e[-1]
        if len(ne) == 0:
            b = 0
        else:
            b = ne[-1]

        if a > b:
            m = e.pop()
        else:
            m = ne.pop()

        if m <= 1:
            return m

        ne.insert(0, ceil(m / 2))
        ne.insert(0, floor(m / 2))

    if len(e) == 0:
        m1 = 0
    else:
        m1 = e.pop()

    if len(ne) == 0:
        m2 = 0
    else:
        m2 = ne.pop()

    return max(m1, m2)


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        n, k = [int(s) for s in input().split()]

        print("Case #{}: {}".format(case, solve(n, k)))




