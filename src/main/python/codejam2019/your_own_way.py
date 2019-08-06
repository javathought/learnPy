t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    p = ['E' if s == 'S' else 'S' for s in input()]

    print("Case #{}: {}".format(i, ''.join(p)))
