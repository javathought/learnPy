import sys

def dfs(adj):
    clock = 0

    def explore(x):
        nonlocal clock
        visited[x] = 1
        pre[x] = clock
        clock = clock + 1
        post[x] = 1
        for w in adj[x]:
            if visited[w] == 0:
                explore(w)
                post[x] += post[w]

        # clock = clock + 1

    for w in range(len(adj)):
        if visited[w] == 0:
            explore(w)


def solve_fibrecut(input):
    global prof

    global visited, pre, post

    data = list(map(int, input.split()))

    n = data[0]
    visited = [0 for _ in range(n)]
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    m = n-1
    data = data[1:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj=[[] for _ in range(n)]

    for (a,b) in edges:
        adj[a].append(b)
        adj[b].append(a)

    dfs(adj)
    mini = min([ max(p, n-p) for p in post])

    return n - mini


if __name__ == '__main__':
    n = int(input())
    visited = [0 for _ in range(n)]
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]


    adj=[[] for _ in range(n)]
    for x in range(n-1):
        a,b = map(int, input().split())

        adj[a].append(b)
        adj[b].append(a)

    dfs(adj)
    mini = min([ max(p, n-p) for p in post])
    print(n - mini)