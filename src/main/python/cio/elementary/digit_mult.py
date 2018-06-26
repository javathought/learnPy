import functools
import operator

foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)


def checkio(number: int) -> int:
    # digits = list(map(lambda c: int(c), list(str(number).replace('0', ''))))
    digits = [int(char) for char in str(number) if char != '0']
    return foldl(operator.mul, 1, digits)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
