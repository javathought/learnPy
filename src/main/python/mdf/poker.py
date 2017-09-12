import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


cave = int(lines[0])
for l in lines[2:]:
    x, y = list(map(int, l.split()))
    cave += y - x

print(cave)
