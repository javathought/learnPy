#Uses python3

import sys


def number_of_components(adj):
    def explore(x, actual):
        visited[x] = 1
        cc[x] = actual
        for w in adj[x]:
            if visited[w] == 0:
                explore(w, actual)

    result = 1
    for w in range(n):
        if visited[w] == 0:
            explore(w, result)
            result = result + 1
    return result - 1


def solve_cc(input):
    global visited
    global cc
    global n
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    cc = [0 for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return number_of_components(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_cc(input))
