def LetterChanges(str):
    # code goes here
    resp = ''
    for c in str:
        if 'a' <= c <= 'z':
            if c == 'z':
               next_c = 'a'
            else:
                next_c = chr(ord(c)+1)
            if next_c in ['a', 'e', 'i', 'o', 'u']:
                next_c = next_c.upper()
            resp = resp + next_c
        else:
            resp = resp + c

    return resp


# keep this function call here
print LetterChanges(raw_input())


