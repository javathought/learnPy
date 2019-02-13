import sys


def interets(lines):
    j = int(lines[0])  # nb jours
    s = int(lines[1])  # solde
    i1=0 # interets methode 1
    i2=0 # interets methode 2
    c=0 # mb jours consécutifs

    for l in lines[2:]:
        s += int(l)
        if (s < 0):
            c +=1
            if c > 2:
                i1 += s/10
            if c > 3:
                i2 += s*3/10
            else:
                i2 += s/5
        else:
            c = 0

    return i1-i2


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    print(interets(lines))
