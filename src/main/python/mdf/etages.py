import sys

lines = []

l = int(input())
n = int(input())

e = []

for _ in range(n):
    e.append(int(input()))

res = 0

while len(e) > 0:
    c = e[0]
    if c == l:
        res += 1
        break;

    for d in e[1:]:
        if c + d == l:
            e.remove(d)
            res += 1
            break
    e.remove(c)

print(res)