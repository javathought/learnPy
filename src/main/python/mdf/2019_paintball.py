lines = []
results = []
i = int(input())
for _ in range(i):
    l = input()
    if l == l[::-1]:
        results.append(l)

print(" ".join(results))
