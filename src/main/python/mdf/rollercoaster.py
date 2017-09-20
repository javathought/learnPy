import sys

n = int(input())

t = []

for _ in range(n):
    t.append(int(input()))

s = sorted(t)

res = ""

for i in range(0, n, 2):
    res += str(s[i+1]) + " " + str(s[i]) + " "

print(res)