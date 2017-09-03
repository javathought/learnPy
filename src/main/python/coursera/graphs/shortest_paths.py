#Uses python3

import sys
import queue


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    prev = [-1 for _ in range(len(adj))]
    distance[s] = 0
    reachable[s] = 1
    q = queue.Queue()
    for i in range(len(adj)):
        for u in range(len(adj)):
            for j, v in enumerate(adj[u]):
                d = distance[u] + cost[u][j]
                if distance[v] > d:
                    reachable[v] = 1
                    distance[v] = d
                    prev[v] = u
                    if i == len(adj) - 1:  # we have a negative weight cyclecycle
                        shortest[v] = 0
                        q.put(v)

    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if shortest[v] == 1:   # not visited in BFS to find infinite
                q.put(v)
                shortest[v] = 0


def solve_shortest(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    rep = ""
    for x in range(n):
        if reachable[x] == 0:
            rep += '*'
        elif shortest[x] == 0:
            rep += '-'
        else:
            rep += str(distance[x])
        rep += "\n"
    return rep

if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_shortest(input))

