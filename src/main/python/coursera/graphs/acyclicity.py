#Uses python3

import sys


def dfs(adj):
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
        post[x] = clock

    for w in range(len(adj)):
        if visited[w] == 0:
            explore(w)


def acyclic(adj):

    dfs(adj)

    for u in range(len(adj)):
        neighbours = adj[u]
        for v in neighbours:
            if post[v] > post[u]:    # post[u] > post[v] always true in a DA(cyclic)G
                return 1

    return 0


def solve_acyclic(input):
    global visited, pre, post, n
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return acyclic(adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_acyclic(input))