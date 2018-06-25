n = int(input())

p = [[] for _ in range(n)]
r = [[0] * n for _ in range(n)]

for i in range(n):
    p[i] = list(input())


def compute():
    for i in range(n):
        for j in range(n):
            r[i][j] = max(r[i][max(j-1, 0)], r[max(i-1, 0)][j])
            if p[i][j] == 'X':
                r[i][j] += 1


def activate():
    i,j = n-1, n-1
    while (i,j) != (0,0):
        p[i][j] = '.'
        if i == 0:
            j -= 1
        elif j == 0 or r[i-1][j] > r[i][j-1]:
            i -= 1
        else:
            j -= 1


r[n-1][n-1] = 1
res = 0

while r[n-1][n-1] > 0:
    r = [[0] * n for _ in range(n)]
    compute()
    res +=1
    activate()


print(res-1)
