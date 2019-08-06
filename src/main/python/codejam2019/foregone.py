t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = [s for s in input()]

    at = ['2' if int(c) == 4 else c for c in n ]
    a = int(''.join(at))
    b = int(''.join(n)) - a

    print("Case #{}: {} {}".format(i, a, b))
