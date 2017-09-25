n = int(input())

p = [[] for _ in range(n)]
r = [[0] * n for _ in range(n)]

for i in range(n):
    p[i] = input()

for i in range(n):
    for j in range(n):
        r[i][j] = max(r[i][max(j-1,0)], r[max(i-1,0)][j])
        if p[i][j] == 'X':
            r[i][j] += 1

print(r[n-1][n-1])
