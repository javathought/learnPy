import sys
import jellyfish as jf

# ajout d'une lettre (arbre -> arbore) a un coût de 2 ;
# - La suppression d'une lettre (globe -> lobe) a un coût de 2 ;
# - Le remplacement d'une lettre par une autre (barbe -> barre) a un coût de 3 ;
# - Et enfin, l'échange de deux lettres consécutives (orbe -> robe) a un coût de 3.


def damerau_levenshtein_distance_isograd(a, b):
    n = len(a)
    m = len(b)
    dist = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if min(i, j) == 0:
                dist[i][j] = max(i, j) * 2
            elif i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                dist[i][j] = min(dist[i - 1][j] + 2,
                                 dist[i][j - 1] + 2,
                                 dist[i - 1][j - 1] + 3 * (a[i - 1] != b[j - 1]),
                                 dist[i - 2][j - 2] + 3)
            else:
                dist[i][j] = min(dist[i - 1][j] + 2,
                                 dist[i][j - 1] + 2,
                                 dist[i - 1][j - 1] + 3 * (a[i - 1] != b[j - 1]))
    return dist[n][m]


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 3
            d[(i, j)] = min(
                d[(i - 1, j)] + 2,  # deletion
                d[(i, j - 1)] + 2,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]


def distance(s1, s2):
    if len(s1) < len(s2):
        return distance(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def levenshtein_try(x, y):
    """Levenshtein edit distance
    :param x:
    :param y: strings
    :returns: distance
    :complexity: `O(|x|*|y|)`
    """
    n = len(x)
    m = len(y)
    #                         initialisation ligne 0 et colonne 0
    A = [[i + j for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if i < n-1 and j< m-1:
                A[i + 1][j + 1] = min( A[i][j + 1] + 2,              # insertion
                                  A[i + 1][j] + 2,              # suppress.
                                  A[i][j] + 3*int(x[i] != y[j]), # substitut.
                                  A[i][j] + 3*int(x[i] == y[j+1] and x[i+1] == y[j]) # switch.
                                  )
            else:
                A[i + 1][j + 1] = min( A[i][j + 1] + 2,              # insertion
                                  A[i + 1][j] + 2,              # suppress.
                                  A[i][j] + 3*int(x[i] != y[j])) # substitut.

    return A[n][m]


if __name__ == '__main__':

    len_dict = int(input())

    mots=[]
    for n in range(len_dict):
        mots.append(input())

    nb_mots_saisis = int(input())

    for m in range(nb_mots_saisis):
        mot = input()
        dist = sys.maxsize
        for m in mots:
            # calcule distance
            # d = jf.damerau_levenshtein_distance(mot, m)
            d = jf.levenshtein_try(mot, m)
            if d < dist:
                dist = d
                proche = m
            elif d == dist and m < proche:
                proche = m

        print(proche)



