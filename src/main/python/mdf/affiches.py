import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


x = int(lines[0])  # stock
n = int(lines[1])  # nombre de jours dans le mois

for l in lines[2:]:
    x -= int(l)

print(x)