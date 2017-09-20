import sys

n = int(input())

t = [["."] * n for _ in range(n)]

car = "*"

for i in range(0,n-2,2):
    d = n-i

    for j in range(d):
        for k in range(d):
            if not (
                        (j==0 and k==0) or (j==0 and k==d-1)
                or
                            (j == d-1 and k == 0) or (j == d-1 and k == d-1)
            ):
                t[i//2+j][i//2+k] = car

    if car == "*":
        car = "#"
    else:
        car = "*"

for i in range(n):
    print("".join(t[i]))
