import sys


def pole_vault(lines):
    n = int(lines[0])  # nb tries
    best = 0
    records = {}

    for l in lines[1:]:
        # aaaaaa 4.25 S
        a, hs, s = l.split()   # a: athlete, h: height, s: success?
        h = float(hs)

        #print(a, h ,s)

        if h > best and s == 'S':
            best = h

        if not a in records:
            records[a] = (0, 0, 0, 0, 0)   # best success, last height, nb tries on last , nb tries on best, total fails

        if h == records[a][1]:
            nbt = records[a][2] + 1
        else:
            nbt = 1

        if s == 'S':
            records[a] = (h, h, nbt, nbt, records[a][4])
        else:
            records[a] = (records[a][0], h, nbt, records[a][3], records[a][4]+1)

    #print("best = " , best , "records = ")
    #print(records)

    win = ""

    best_ath = None
    for ath, r in records.items():
        #print(best, ath, r)
        if r[0] == best:
            if best_ath == None:
                win = ath
                best_ath = r
            else:
                if r[3] < best_ath[3]:
                    win = ath
                    best_ath = r
                if r[3] == best_ath[3] and r[4] < best_ath[4]:
                    win = ath
                    best_ath = r
                if r[3] == best_ath[3] and r[4] == best_ath[4]:
                    win = "KO"

    #print(win)
    return win


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    print(pole_vault(lines))
