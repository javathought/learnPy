import numpy as np

def checkio(game_result):

    def win(tab, car):
        res = False
        for c in tab:
            res |= all([x == car for x in c])
        return res

    def winDiag(tab, car):
        d1 = tab[[0, 1, 2], [0, 1, 2]]
        d2 = tab[[0, 1, 2], [2, 1, 0]]
        return all([x == car for x in d1]) or all([x == car for x in d2])


    x_result = []
    for r in game_result:
        x_result.append([x for x in r])

    result = np.array(x_result)

    t = result.transpose()

    if win(result, 'X') or win(t, 'X') or winDiag(t, 'X'):
        return "X"

    if win(result, 'O') or win(t, 'O')or winDiag(t, 'O'):
        return "O"


    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

