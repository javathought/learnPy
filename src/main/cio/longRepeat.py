def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    cur = line[0]
    curlen = 0
    max = 0
    for c in line:
        if c == cur:
            curlen += 1
        else:
            cur = c
            if curlen > max:
                max = curlen
            curlen = 1

    return max

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')