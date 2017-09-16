#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

def mouv(p, m):
    tuple(x + y for x, y in zip(p, m))


size = int(lines[0])
nb = int(lines[1])


if (nb < size):
    print(nb, 0)
else:
    mvts = lines[2:nb - size + 3]
    print(mvts)
    pos = (size - 1, 0)
    print("pos = " + str(pos))
    m = (0,0)

    for mv in mvts:   # mvts[0][0:nb - size + 1]:  # if mbt on 1 line
        print("mv = " + mv)
        if mv == 'D':
            m = (1, 0)
        if mv == 'G':
            m = (-1, 0)
        if mv == 'H':
            m = (0, -1)
        if mv == 'B':
            m = (0, 1)

        print(m)

        pos = tuple(x + y for x,y in zip(pos, m))

    print("%d %d" % pos)

# print( (6,0) + (-1, 1))
# print( tuple(x + y for x,y in zip((0,-1,7), (3,4,-7))) )
