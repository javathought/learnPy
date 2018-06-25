def safe_pawns(pawns: set) -> int:
    safe = 0
    for pawn in pawns:
        col = pawn[:1]
        line = pawn[1:]
        def_left = chr(ord(col)-1) + str(int(line)-1)
        def_right = chr(ord(col)+1) + str(int(line)-1)
        if def_left in pawns or def_right in pawns:
            safe += 1;
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")