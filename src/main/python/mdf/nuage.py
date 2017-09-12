import sys
from collections import Counter

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

tags = lines[1:]

for m in Counter(tags).most_common(5):
    print(m[0], m[1])