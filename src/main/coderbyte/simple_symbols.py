def SimpleSymbols(str):
    # code goes here
    prev = ''
    prev_is_letter = False
    for c in str:
        if prev_is_letter and c != '+':
            return 'false'
        if 'a' <= c <= 'z':
            prev_is_letter = True
            if prev != '+':
                return 'false'
        else:
            prev_is_letter = False

        prev = c
    if prev_is_letter:
        return 'false'
    return 'true'


# keep this function call here
print(SimpleSymbols(input()))


