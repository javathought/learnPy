import sys

h = int(input())
l = int(input())

t = [[] * l for _ in range(h)]
visited = [[0] * l for _ in range(h)]

for li in range(h):
    sl = input()
    t[li] = [x for x in sl]

ld = 0
hd = 0

for i in range(h):
    for j in range(l):

        if t[i][j] == 'x':
            ld = i
            hd = j

        # if t[i][j] != '*':
        #
        #     v = 0
        #     if i-1 >= 0 and j-1 >= 0 and t[i-1][j-1] == '*':
        #         v += 1
        #     if i-1 >= 0 and t[i-1][j] == '*':
        #         v += 1
        #     if i-1 >= 0 and j+1 < l and t[i-1][j+1] == '*':
        #         v += 1
        #
        #     if j-1 >= 0 and t[i][j-1] == '*':
        #         v += 1
        #     if j+1 < l and t[i][j+1] == '*':
        #         v += 1
        #
        #     if i+1 < h and j-1 >= 0 and t[i+1][j-1] == '*':
        #         v += 1
        #     if i+1 < h and t[i+1][j] == '*':
        #         v += 1
        #     if i+1 < h and j+1 < l and t[i+1][j+1] == '*':
        #         v += 1
        #
        #     t[i][j] = str(v)

nb = 1

voisins = [(ld,hd)]
visited[ld][hd] = 1

v = 1
while len(voisins) > 0:
    i,j = voisins[0]
    if i - 1 >= 0 and j - 1 >= 0 and visited[i - 1][j - 1] == 0:
        v += 1
        if t[i - 1][j - 1] != '*':
            voisins.append((i - 1, j - 1))
            t[i - 1][j - 1] = 'z'
        visited[i - 1][j - 1] = 1
    if i - 1 >= 0 and visited[i - 1][j] == 0:
        v += 1
        if t[i - 1][j] != '*':
            voisins.append((i - 1, j))
            t[i - 1][j] = 'z'
        visited[i - 1][j] = 1
    if i - 1 >= 0 and j + 1 < l and visited[i - 1][j + 1] == 0:
        v += 1
        if t[i - 1][j + 1] != '*':
            voisins.append((i - 1,j + 1))
            t[i - 1][j + 1] = 'z'
        visited[i - 1][j + 1] = 1
    if j - 1 >= 0 and visited[i][j - 1] == 0:
        v += 1
        if t[i][j - 1] != '*':
            voisins.append((i, j - 1))
            t[i][j - 1] = 'z'
        visited[i][j - 1] = 1
    if j + 1 < l and visited[i][j + 1] == 0:
        v += 1
        if t[i][j + 1] != '*':
            voisins.append((i,j + 1))
            t[i][j + 1] = 'z'
        visited[i][j + 1] = 1
    if i + 1 < h and j - 1 >= 0 and visited[i + 1][j - 1] == 0:
        v += 1
        if t[i + 1][j - 1] != '*' :
            voisins.append((i + 1, j - 1))
            t[i + 1][j - 1] = 'z'
        visited[i + 1][j - 1] = 1
    if i + 1 < h and visited[i + 1][j] == 0:
        v += 1
        if t[i + 1][j] != '*':
            voisins.append((i + 1, j))
            t[i + 1][j] = 'z'
        visited[i + 1][j] = 1
    if i + 1 < h and j + 1 < l and visited[i + 1][j + 1] == 0:
        v += 1
        if t[i + 1][j + 1] != '*':
            voisins.append((i + 1,j + 1))
            t[i + 1][j + 1] = 'z'
        visited[i + 1][j + 1] = 1

    voisins.remove((i, j))

# for li in t:
#    local_print("".join(li))

print(v)
