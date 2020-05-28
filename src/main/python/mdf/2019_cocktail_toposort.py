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
        post[x] = clock

    for w in adj:
        if visited[w] == 0:
            explore(w)


def toposort(adj):
    global visited, post, pre

    visited = {k: 0 for k in adj.keys() }
    pre = {k: 0 for k in adj.keys() }
    post = {k: 0 for k in adj.keys() }
    dfs(adj)
    # sort = sorted(post, key=lambda p: p, reverse=True)
    sort = {k: v for k, v in sorted(post.items(), key=lambda item: item[1], reverse=True)}
    order = [ k for k in sort.keys()]
    # order = []
    #write your code here
    return " < ".join(order)


def acyclic(adj):
    global visited, post, pre
    visited = {k: 0 for k in adj.keys() }
    pre = {k: 0 for k in adj.keys() }
    post = {k: 0 for k in adj.keys() }

    dfs(adj)

    for u in adj.keys():
        neighbours = adj[u]
        for v in neighbours:
            if post[v] > post[u]:    # post[u] > post[v] always true in a DA(cyclic)G
                return 1

    return 0


def solve_toposort(input):
    data = input.split()
    n, m = list(map(int, data[0:2]))
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {k: [] for k in set(data)}
    for (a, b) in edges:
        # if not a in adj:
        #     adj[a] = []
        adj[a].append(b)

    if acyclic(adj) == 1:
        return "KO"

    return toposort(adj)


n, m = [int(i) for i in input().split()]

graph = "{} {}".format(n, m)

for _ in range(m):
    graph = graph + " " + input()


print(solve_toposort(graph))

# 5 4
# club-mate pamplemousse
# pamplemousse grenadine
# mojito club-mate
# fraise club-mate

# yuzu < pomelos < noix-de-coco < icaque
# icaque < pomelos < yuzu < noix-de-coco

# reine-claude < prune-de-cythere < patisson < pain-de-singe < cucamelon
# prune-de-cythere < pain-de-singe < reine-claude < cucamelon < patisson
