import sys
import string
import operator

# line = sys.stdin

# max(string.ascii_lowercase, key=poids)
# def poids(letter):


def maxbalise(xml):
    prof = 0
    skip = False
    poids = { l:0 for l in string.ascii_lowercase }
    # poids = {}

    for l in xml:
        if skip:
            skip = False
            continue
        if l == '-':
            prof -= 1
            skip = True
        else:
            prof += 1
            if not l in poids:
                poids[l] = 0
            poids[l] += 1/prof

    s = sorted(poids.items(), key=operator.itemgetter(1), reverse=True)
    return s[0][0]


if __name__ == '__main__':
    line = input()
    print(maxbalise(line))