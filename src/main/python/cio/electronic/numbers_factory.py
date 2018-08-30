import itertools

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

def checkio(number):
    div = 9

    chiffres = []

    while number > 1:
        if number % div == 0:
            chiffres.append(str(div))
            number = number // div
        else:
            div = div - 1
        if div == 1 : #and number > 1:
            return 0

    print(int("".join(list(reversed(chiffres)))))
    return int("".join(list(reversed(chiffres))))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(60) == 256, "personal example"
    assert checkio(18) == 29, "18 example"
    assert checkio(20) == 45, "20 example"
    assert checkio(24) == 38, "24 example => 38 not 46"
    assert checkio(54) == 69, "54 example"
    assert checkio(560) == 2578, "5th example"
    assert checkio(1536) == 3888, "5th example"
