# Numeral	Value
# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1,000 (mille)

conv = [
    ['I', 'V'],
    ['X', 'L'],
    ['C', 'D'],
    ['M', ' ']
]


def digit_to_roman(value, unit):
    digit = int(value)
    if digit <= 3:
        return conv[unit][0] * digit
    elif digit == 4:
        return conv[unit][0] + conv[unit][1]
    elif 5 <= digit <= 8:
        return conv[unit][1] + conv[unit][0] * (digit - 5)
    else:
        return conv[unit][0] * (10 - digit) + conv[unit+1][0]


def to_roman(arabic, unit):
    if len(arabic) == 0:
        return ""

    return digit_to_roman(arabic[0], unit) + to_roman(arabic[1:], unit - 1)


def checkio(data):
    arabic = str(data)
    return to_roman(arabic, len(arabic) - 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(571) == 'DLXXI', '571'
    assert checkio(1131) == 'MCXXXI', '1131'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')