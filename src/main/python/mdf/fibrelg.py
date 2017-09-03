import sys
from math import sqrt


def findclosest(g, list_ord):
    # closest = Nil
    dist = sys.maxsize
    for m in list_ord:
        for n in g:
            d = distance(n,m)
            if d < dist:
                dist = d
                rep = (n,m)
    return rep


def distance(a,b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if __name__ == '__main__':

    nb_ords = int(input())

    ords=[]
    for n in range(nb_ords):
        a,b = input().split()
        #print(a)
        ords.append((float(a),float(b)))

    dist = 0.0

    g = [ords[0]]
    ords.remove(ords[0])
    while not len(ords) == 0:
        n,m = findclosest(g, ords)
        dist += distance(n,m)
        g.append(m)
        ords.remove(m)

    print(dist)
