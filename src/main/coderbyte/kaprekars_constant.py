def KaprekarsConstant_acc(num, acc):
    # code goes here

    if num == 6174:
        return acc

    chiffres = (['0' for _ in range(4)] + sorted(str(num)))[-4:]

    b = int(''.join(chiffres))
    a = int(''.join(reversed(chiffres)))

    n = a - b

    return KaprekarsConstant_acc(n, acc + 1)


def KaprekarsConstant(num):
    return KaprekarsConstant_acc(num, 0)


if __name__ == '__main__':
    # keep this function call here
    print(KaprekarsConstant(input()))
