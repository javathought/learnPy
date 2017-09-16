import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

#n = int(lines[0])
total = 0
for l in lines[1:]:
    total += int(l)

print(total)

#  Other solution :
# n = int(input())
# print(sum(int(input()) for _ in range(n)))

