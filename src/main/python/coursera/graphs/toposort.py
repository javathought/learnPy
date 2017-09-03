#Uses python3

import sys


def dfs(adj): #, used, order, x):
    clock = 0

    def explore(x):
        nonlocal clock
        visited[x] = 1
        clock = clock + 1
        pre[x] = clock
        for w in adj[x]:
            if visited[w] == 0:
                explore(w)
        clock = clock + 1
        post[x] = (x,clock)

    for w in range(len(adj)):
        if visited[w] == 0:
            explore(w)


def toposort(adj):
    used = [0] * len(adj)
    global visited, post, pre
    visited = [0] * len(adj)
    pre = [0] * len(adj)
    post = [0] * len(adj)
    dfs(adj)
    sort = sorted(post, key=lambda p: p[1], reverse=True)
    order = [ p[0] + 1 for p in sort]
    # order = []
    #write your code here
    return order


def solve_toposort(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return toposort(adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    order = solve_toposort(input)
    for x in order:
        print(x + 1, end=' ')
