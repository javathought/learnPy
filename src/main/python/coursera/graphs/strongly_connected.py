#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_scc(adj):
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
        post[x] = (x, clock)

    def dfs(adj):  # , used, order, x):

        for w in range(len(adj)):
            if visited[w] == 0:
                explore(w)

    global visited, post, pre
    visited = [0] * len(adj)
    pre = [0] * len(adj)
    post = [0] * len(adj)
    scc = [0] * len(adj)

    dfs(adj)

    sort = sorted(post, key=lambda p: p[1], reverse=False)  # because dfs(adj) and not dfs(reverse(adj)
    order = [p[0] for p in sort]

    # reset visited for SCC
    visited = [0] * len(adj)

    curr = 0

    for v in order:
        if visited[v] == 0:
            curr += 1
            explore(v)

    result = curr
    #write your code here
    return result


def solve_number_of_scc(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        # adj[b - 1].append(a - 1)
    # rev_adj = [ (n[1], n[0]) for n in adj]
    return number_of_scc(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_number_of_scc(input))
