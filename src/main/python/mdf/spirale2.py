import sys

n = int(input())

if (n-1) % 4 == 0:
    car = "#"
else:
    car = "="

t = [[car] * n for _ in range(n)]

for i in range((n-1)//2):
    if car == "=":
        car = "#"
    else:
        car = "="

    for j in range(i+1, n-1-i):
        for k in range(i, n-1-i):
            t[j][k] = car

    t[j+1][i] = car

for i in range(n):
    print("".join(t[i]))