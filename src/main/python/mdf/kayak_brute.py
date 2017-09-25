n = int(input())

p = [[] for _ in range(n)]

res = 0

for i in range(n):
    p[i] = [x for x in input()]

def max_porte(l,c):
    cur = 0
    if p[l][c] == 'X':
        cur = 1
    if (l == n-1 and c == n-1):
        return cur
    elif (l == n-1):
        return cur + max_porte(l, c + 1)
    elif (c == n-1):
        return cur + max_porte(l + 1, c)
    else:
        return cur + max(max_porte(l+1,c), max_porte(l,c+1))

print(max_porte(0,0))