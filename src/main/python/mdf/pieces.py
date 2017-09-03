import sys

# solution for unlimited stock
def sumtototal(total, coins_list):
    s = [0]
    # dyn_stock = [0 for _ in range(total + 1)]
    # for (c_stock, c_val) in coins_list:
    #     dyn_stock[c_val] = c_stock
    for i in range(1, total + 1):
        s.append(-1)
        for a in coins_list:
            (coin_stock, coin_val) = a
            if i - coin_val >= 0 and s[i - coin_val] != -1 and (s[i] > s[i - coin_val] or s[i] == -1):
                # if dyn_stock[coin_val] > 0:
                    s[i] = 1 + s[i - coin_val]
                    # dyn_stock[coin_val] -= 1
                # else:
                #     s[i] = s[coin_val] + s[i - coin_val]

    print(s)
    return s[total]

def rec_coins(total, coins_list, nb):
    if total == 0:
        return nb
    if len(coins_list) == 0:
        return sys.maxsize

    pieces = []
    for i in range(coins_list[0][0]+1):
        coin_val = coins_list[0][1]
        val_involved = i * coin_val
        pieces.append(rec_coins(total-val_involved, coins_list[1:], nb+i))

    pieces.sort()

    return pieces[0]

def solve_coins(puzzle_lines):

    m = int(puzzle_lines[0])   # amount : between 1 & 25000
    t = int(puzzle_lines[1])   # nb types of coins : between 1 & 10
    data = puzzle_lines[2:]
    stock_string = [s for s in reversed([l.split() for l in data])] # n,v :nb coins of type, value of type
    # stock_string = [l.split() for l in data] # n,v :nb coins of type, value of type
    stock = [(int(c[0]), int(c[1])) for c in stock_string]

    res = rec_coins(m, stock, 0)

    if res == sys.maxsize:
        res = "IMPOSSIBLE"

    print(res)

    return res

if __name__ == '__main__':

    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    solve_coins(lines)
