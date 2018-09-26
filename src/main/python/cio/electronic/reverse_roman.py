romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def reverse_roman(roman_string):
    i = 0
    prec = 0
    for letter in roman_string:
        current = romans[letter]

        i += current
        if prec < current:
            i -= prec * 2 # already added once
        prec = current

    return i


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('DLXXI') == 571, '571'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');