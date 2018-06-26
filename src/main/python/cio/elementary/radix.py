def checkio(str_number: str, radix: int) -> int:

    digits = [char for char in str_number]
    number = 0
    for d in digits:
        if d.isnumeric():
            if int(d) >= radix:
                return -1
            digit = int(d)
        if d.isalpha():
            if ord(d) > ord('A') + radix - 10:
                return -1
            digit = ord(d) - ord('A') + 10
        number = number * radix + digit

    return number

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

