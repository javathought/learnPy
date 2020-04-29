import math
# import numpy

limit = 1000000000

def solve():
    prog = input()
    w, h = 1, 1

    fact = [1]
    rapport = 1
    for c in prog:
        if c in '23456789':
            fact.append(int(c))
            rapport *= int(c)

        if c == ')':
            r = fact.pop()
            rapport //= r

        if c == 'S':
            h = (h+rapport) % limit

        if c == 'E':
            w = (w+rapport) % limit

        if c == 'N':
            h = (h-rapport) % limit

        if c == 'W':
            w = (w-rapport) % limit

    if w == 0:
        w = limit

    if h == 0:
        h = limit

    return w, h


if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        w, h = solve()
        print("Case #{}: {} {}".format(case, w, h))

