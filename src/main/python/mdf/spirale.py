import sys

n = int(input())

t = [["="] * n for _ in range(n)]


#s = gbdh
s = 'h'

l = (n-1)//2
c = (n-1)//2
t[l][c] = '#'
sd = 0
for i in range(n-1):
    for j in range(i):
        if s == 'g' or s == 'd':
            l += sd
        if s == 'h' or s == 'b':
            c += sd

        t[c][l] = "#"

    if s == 'h':
        s = 'g'
        sd = -1
    elif s == 'g':
        s = 'b'
        sd = 1
    elif s == 'b':
        s ='d'
        sd = 1
    elif s == 'd':
        s = 'h'
        sd = -1


if (n-1) % 4 == 0:
    for i in range(n):
        t[0][i] = "#"
        t[i][n-1] = "#"
else:
    for i in range(n-2):
        t[i+2][0] = "#"


for i in range(n):
    print("".join(t[i]))
