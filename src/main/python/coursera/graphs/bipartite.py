#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here

    s = 0

    dist = [-1 for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]   # not necessary for assigment
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    while (not q.empty()):
        u = q.get()
        for v in adj[u]:
            if dist[v] == -1:
                q.put(v)
                dist[v] = dist[u]+1
                prev[v] = u   # not necessary for assigment

    # check if on same layer there's an edge : not bipartite
    # if exits an edge with ancestor layer (< n-1), vertice would have been on previous layer (n) or an ancestor
    for u in range(len(adj)):
        if dist[u] == -1:
            return 0    # vertice not linked
        for v in adj[u]:
            if dist[u] == dist[v]:
                return 0

    return 1

def solve_bipartite(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return bipartite(adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    print(solve_bipartite(input))
