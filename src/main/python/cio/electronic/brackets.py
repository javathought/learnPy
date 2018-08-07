def checkio(expression):
    pile = []

    for c in expression:
        if c in {')', '}', ']'}:
            if len(pile) > 0 and c == pile[-1]:
                pile = pile[:-1]
            else:
                return False
        if c == '(':
            pile.append(')')
        if c == '{':
            pile.append('}')
        if c == '[':
            pile.append(']')

    if len(pile) == 0:
        return True

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(")") == False, "Only close"
    assert checkio("(((("
                   "[[["
                   "{{{3"
                   "}}}"
                   "]]]]"
                   "))))") == False, "Only close"
    assert checkio("2+3") == True, "No brackets, no problem"
