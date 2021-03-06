# The list of banned words are as follows:

    # sum
    # import
    # for
    # while
    # reduce

def checkio(data):
    if len(data) == 0:
        return 0
    return data[0] + checkio(data[1:])

if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6, " 1+2+3"
    assert checkio([2, 2, 2, 2, 2, 2]) == 12, "6*2"