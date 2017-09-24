import sys

n = int(input())

t = [[] for _ in range(n)]
r = [0 for _ in range(n)]
visited = [0 for _ in range(n)]
power = [0 for _ in range(n)]
vassals = [set() for _ in range(n)]


def dfs(adj):

    def explore(x):
        visited[x] = 1
        vassals[x].add(x)
        for w in adj[x][1:]:
            if visited[w] == 0:
                explore(w)
            vassals[x].update(vassals[w])

        # clock = clock + 1

    for w in range(len(adj)):
        if visited[w] == 0:
            explore(w)


for i in range(n):
    t[i] = list(map(int, input().split()))

dfs(t)

for i in range(n):
    power[i] = sum([t[v][0] for v in vassals[i]])

print(max(power))
